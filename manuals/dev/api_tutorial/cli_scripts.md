---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: api_tutorial/cli_scripts
category: manuals
---

# API Tutorials: CLI Scripting

In this tutorial you will learn how to use the CLI's scripting capabilities in order to automatize your experiment.

In addition to simply using the API, you will also create archives for executable archives

## Experiment Overview

Our experiment shall be conducted as follows:

1. Create a topology consisting of two container-based elements that are connected to each other. Set a delay of 100ms per direction
2. Prepare and start the elements
3. Install Python on all elements
4. Install our test software on all elements
5. Run our test software and store the result in the device's custom status
6. Collect the results
7. Clean up.

The test software is a simple python-based client-server tool that measures the delay between both devices. This is not that interesting, but should be a good example for an automated experiment.

## Preparation

First, you should download the necessary files: 

* The python installer executable archive [(download here)](https://master.tomato-lab.org/web_resources/executable_archive/install_python)
* Our test software [(download here)](../nw_measurer.tar.gz)

{:.alert alert-info}
The Python installer archive has been created using the [Executable archive packet manager](../../tools/getpackages).

In the following, these files are assumed to be available at `/tmp/install_python.tar.gz` and `/tmp/nw_measurer.tar.gz`


## Developing the Script

This project consists of one script, available at `~/measure_test_experiment.py`. Simply create an empty file for this. Since we use the CLI, we can access all API calls as global variables

You should keep in mind that this script has to completely function on its own. If you are unsure about an API and its effects, you can look it up in the API reference, or you can try it out via the CLI.

In the following, we will develop a single script. If not stated otherwise, the final script will be a concatenation of all snippets in this tutorial.

{:.alert .alert-info}
It may be useful to have a sandbox topology when developing scripts.

## Step 0: Set-Up

This step is optional since we just define some constants. However, it is easier to change if we do it at the beginning of the script.

{% highlight python %}
# software path
python_installer_file = "/tmp/install_python.tar.gz"
test_software = "/tmp/nw_measurer.tar.gz"

# temporary directory to work in
import os
import random
tmp_dir = "/tmp/auto_experiment%d" % random.randint(0,10000)
os.mkdir(tmp_dir)

# function for better-looking run statements
import subprocess
def run(*cmd):
  subprocess.call(cmd)
{% endhighlight %}


## Step 1 and 2: Topology Creation and Start

The following code will generate our desired topology:

{% highlight python %}
# create topology
top_id = topology_create()["id"]

# create test elements
# we should separate between client and server at this point to make things easier
server_element = element_create(top_id, "container", None, {"name": "server"})["id"]
client_element = element_create(top_id, "container", None, {"name": "client"})["id"]

# create interfaces and connections. Set IP addresses and delay.
if1 = element_create(top_id, "container_interface", server_element, {"ip4address": "10.0.0.1/24"})["id"]
if2 = element_create(top_id, "container_interface", client_element, {"ip4address": "10.0.0.2/24"})["id"]
conn = connection_create(if1, if2, {"delay_from": 100, "delay_to": 100})

print "starting topology"

# start the topology
topology_action(top_id, "start")
{% endhighlight %}

## Step 3 and 4: Install Software

To install Python, we can simply upload the respective archive. However, our software is not in an executable archive yet, so we should also pack it.

{% highlight python %}
# install python
print "install python: 1/2"
upload_and_use_rextfv(server_element, python_installer_file)
print "install python: 2/2"
upload_and_use_rextfv(client_element, python_installer_file)

# while the python installer is running on our elements, let's
print "creating sw installer"
# first, create auto_exec.sh for the installer
# prepare the software installer
auto_exec = os.path.join(tmp_dir, "auto_exec.sh")
auto_exec_content = """#!/bin/bash
tar axf $archive_dir/%s -C /test_software
""" % os.path.basename(test_software)

with open(auto_exec, "w+") as f:
  f.write(auto_exec_content)
# then, create the archive
sw_installer = os.path.join(tmp_dir, "install_testsw.tar.gz")
run("tar", "-C", tmp_dir, "-czf", sw_installer, os.path.join(tmp_dir, os.path.basename(test_software)), auto_exec)

# wait for python installer to finish
import time
print "waiting for Python installer to finish"
for element_id in (server_element, client_element):
	while True:
	  time.sleep(2)
		run_status = element_info(element_id)["rextfv_run_status"]
		if run_status["done"]:
			break

# install sw installer. since the start script doesn't take long,
# there is no need to run them in parallel
print "installing test sw: 1/2"
upload_and_use_rextfv(server_element, sw_installer, True)
print "installing test sw: 2/2"
upload_and_use_rextfv(client_element, sw_installer, True)
{% endhighlight %}

## Step 5: Start the Experiment

To start the experiment, we create two executable archives, one starting the server, and one starting the client.
We upload these to their respective elements, making sure that the server is started before the client.

The server start script opens the server in a separate process. The client start script shall pipe the standard output of the client to the custom status.

{% highlight python %}
# create starter archives
content_server = """#!/bin/bash
cd /test_software
./server.py&
"""
content_client = """#!/bin/bash
cd /test_software
archive_setstatus $(./client.py 10.0.0.1)
"""

with open(auto_exec, "w") as f:
  f.write(content_server)
server_starter = os.path.join(tmp_dir, "start_server.tar.gz")
run("tar", "-C", tmp_dir, "-czf", server_starter, auto_exec)

with open(auto_exec, "w") as f:
  f.write(content_client)
client_starter = os.path.join(tmp_dir, "start_client.tar.gz")
run("tar", "-C", tmp_dir, "-czf", server_starter, auto_exec)

# now, start the software
# the server starter runs the server in a separate process, so we can wait for it
# we want to wait for the client to terminate before continuing
print "starting experiment"
upload_and_use_rextfv(server_element, server_starter, True)
upload_and_use_rextfv(server_element, client_starter, True)
{% endhighlight %}

## Step 6: Collect and Print Data

We know that the client has finished. We can simple access the element's custom status and print it as the result:
{% highlight python %}
result = element_info(client_element)["rextfv_run_status"]["custom"]
print "experiment complete!"
print ""
print "        %s" % result
print ""
{% endhighlight %}

## Step 7: Clean Up

Now, we should to tear down the topology and remove the temporary directory as well.

{% highlight python %}
print "cleaning up..."
# remove tmp dir
import shutil
shutil.rmtree(tmp_dir)

# remove topology
topology_action(top_id, "stop")
topology_remove(top_id)
{% endhighlight %}

## Execute

Now, we have a script. To execute it, we run the CLI with the respective parameters:

`./tomato.py -h master.tomato-lab.org -f ~/measure_test_experiment.py`

You will be prompted for your login, and the experiment will be conducted. Congratulations!

## Conclusion

You have just run an automated experiment using the CLI's scripting capabilities. Of course, you can test more complex software and more complex topologies with it, and use a more closed feedback loop. Now, you know almost everything you need to know to conduct automated tests with ToMaTo.

If you need more ideas, you can check out our examples!

You may also want to catch errors and repeat some things if they fail, but this is rather difficult for CLI scripts. For more advanced scripts, you should use ToMaTo as a library for your own Python program.

{:.alert .alert-info}
The full script is available for download [here](../measurer_experiment.py). Remember to update the first two lines to the correct paths!

## Continue

In the [next tutorial](../api_lib), you will learn how to connect your independent Python app to the ToMaTo API.

