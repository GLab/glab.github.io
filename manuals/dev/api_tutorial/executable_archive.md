---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: api_tutorial/executable_archive
category: manuals
---

# API Tutorial: Import and Executable Archives

Welcome to the third API tutorial. In this tutorial, you will learn how to import a topology using the CLI, how to upload an executable archive, and how to observe the status of the archive.

## Preparation

For this tutorial, you need to files:
* The [domonstration topology export](../introduction_demonstration.tomato4.json)
* The [demonstration executable archive](../demo_archive.tar.gz)

Please download them now. Open a CLI instance. In the following, the filenames are assumed to be `/tmp/introduction_demonstration.tomato4.json` and `/tmp/demo_archive.tar.gz`. If you use different paths, please update them in the commands.

You should also invastigate the demonstration executable archive to understand what it will do: Wait 120 minutes, then set a custom status.

## Importing the topology

ToMaTo offers two API calls for import and export of topologies: `topology_import` and `topology_export`. The export function adds a version information to the topology and strips it of read-only attributes. The import function translates an old export into an up-to-date one and then creates a topology out of it.

In order to be able to import the topology file, we first have to read the file from the disk, and then parse the JSON document to a Python dict structure.

{% highlight python %}
>>> with open("/tmp/introduction_demonstration.tomato4.json", "r") as f:
...   file_content = f.read()
>>> import json
>>> exported_topology = json.loads(file_content)
{% endhighlight %}

In a next step, we can import the topology. we should save the result:
{% highlight python %}
>>> topology_id, id_mapping, errors = topology_import(exported_topology)
{% endhighlight %}

You now have three result variables:
* `topology_id` contains the new topology's ID
* `id_mapping` is a mapping from the IDs in the import to the IDs of the new elements and connections. This can help you identifying the new elements. Since IDs have to be unique on the testbed, the old IDs cannot be used in the new topology.
* `errors contains error messages during the import. You should check if you have received error messages.

## Finding the Container Element

We want to use the container-based element in this topology to upload executable archives to.

You have at least three options how to find the target element now. For practice, let's play through all of them:

### Using the ID Mapping

Open the topology export file with an editor and locate the element with the name "Container-Based Debian". Then read its ID. Then, run the following code
{% highlight python %}
# Lines starting with "#" are comments. You do not need to type them in the CLI.
# First, save the ID you just found as the variable "src_id".

# Now, let's transform the ID mapping to a better-usable format:
>>> id_mapping = {src:dst for src,dst in id_mapping}

# And now you can use the resulting dict to directly query the new ID:
>>> element_id = id_mapping[src_id]
{% endhighlight %}

### Inspecting the Topology

Since you know there is only container-based element in the topology, just search for it:

{% highlight python %}
>>> for element in topology_info(topology_id, True)["elements"]:
>>>  if element["type"] == "container":
>>>    element_id = element["id"]
{% endhighlight %}

### Using the Topology Editor

As mentioned multiple times, the editor can really help you in addition to the CLI. Enable _Show IDs_ in the topology editor's _Options_ tab, right-click on the container-based element, and read its ID.


## Preparing the Element

Now, you should prepare the respective element.

{% highlight python %}
>>> element_action(element_id, "prepare")
{% endhighlight %}


## Uploading the Archive - Manually

At this point, you should understand how uploading works. First, you need some information about the element's host:

{% highlight python %}
>>> el_info = element_info(element_id)
>>> urlinfo = {"hostname": el_info["host_info"]["address"], "port": el_info["host_info"]["fileserver_port"]}
{% endhighlight %}

Now, you can request an _upload grant_ to upload your file. A grant is a one-time access key for accessing the host's fileserver for the respective element. Grants only have a limited lifetime, and only one grant can exist for an element at a given time.

{% highlight python %}
>>> urlinfo["grant"] = api.element_action(element_id, "rextfv_upload_grant")
{% endhighlight %}

This stores the grant right in the `urlinfo` dict that we now use to build a URL to upload our file to:

{% highlight python %}
# build the URL from urlinfo
>>> upload_url = "http://%(hostname)s:%(port)s/%(grant)s/upload" % urlinfo

# upload the file
>>> upload(upload_url, "/tmp/demo_archive.tar.gz")
{% endhighlight %}

You can use any HTTP client to upload the file now, but you should read the API. The CLI, and also the ToMaTo library, has a built-in upload function that can send the respective HTTP request that we were using here.

When you are done uploading the archive, you can use it:

{% highlight python %}
>>> element_action(element_id, "rextfv_upload_use")
{% endhighlight %}

## Starting the Element and Waiting for the Execution

Since the element is in prepared state, automatic execution will happen as soon as we start it.

Let's remember what the archive does: wait two minutes, and then set a custom status. This waiting is for demonstration purposes: a real archive may take some time in order to do its work, like installing software.

To start the element, run 
{% highlight python %}
>>> element_action(element_id, "start")
{% endhighlight %}

And to see the status of execution:
{% highlight python %}
>>> print element_info(element_id)["rextfv_run_status"]
{% endhighlight %}

You will see the values described [here](../../rextfv/auto_exec#run_status).

You can now wait until the execution is finished and see the custom status appear in the element info.

{:.alert .alert-info}
Uploading images works the same way, but using the `upload_grant` and `upload_use` actions instead.


## Uploading the Archive - With Help from the Library

The library, which is also loaded in the CLI, has functions that simplify uploading:

{% highlight python %}
>>> upload_and_use_rextfv(element_id, "/tmp/demo_archive.tar.gz", wait_until_finished=True)
{% endhighlight %}

The `wait_until_finished` argument can let this call block until the execution of the start script has ended. This may come in handy in some situations, but you may want to avoid it when controlling mutliple elements simultaneously.

{:.alert .alert-info}
Uploading images can be done via `upload_and_use_images`.

## Finishing

You are now done, so please clean up:
{% highlight python %}
>>> topology_action(topology_id, "destroy")
>>> topology_remove(topology_id)
{% endhighlight %}

## Conclusion

[TODO]

## Continue

[TODO]

