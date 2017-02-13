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

# create topology
top_id = topology_create()["id"]

# create test elements
# we should separate between client at server at this point to make things easier
server_element = element_create(top_id, "container", None, {"name": "server"})["id"]
client_element = element_create(top_id, "container", None, {"name": "client"})["id"]

# create interfaces and connections
if1 = element_create(top_id, "container_interface", server_element)["id"]
if2 = element_create(top_id, "container_interface", client_element)["id"]
conn = connection_create(if1, if2, {"delay_from": 100, "delay_to": 100})

print "starting topology"

# start the topology
topology_action(top_id, "start")

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
print "installing test sw: 1/2"
upload_and_use_rextfv(client_element, sw_installer, True)

# create starter archives
content_server = """#!/bin/bash
cd /test_software
./server.py&
"""
content_client = """#!/bin/bash
cd /test_software
archive_setstatus $(./client.py)
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


result = element_info(client_element)["rextfv_run_status"]["custom"]
print "experiment complete!"
print ""
print "        %s" % result
print ""

print "cleaning up..."
# remove tmp dir
import shutil
shutil.rmtree(tmp_dir)

# remove topology
topology_action(top_id, "stop")
topology_remove(top_id)

