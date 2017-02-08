---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: api_tutorial/introduction
category: manuals
---

# API Tutorial: Introduction

Welcome to the API introduction. In this tutorial, you will learn how to connect the CLI to ToMaTo, how to query your current data with it, and how to use the graphical topology editor while scripting.

Please make sure you have installed the [ToMaTo tools](../../tools) before you continue.

{:.alert .alert-info}
This tutorial requires you to have a valid user account in a ToMaTo testbed.

{:.alert .alert-warning}
This tutorial is interactive. You must have access to a Linux computer. You will be asked to use certain functions, but to see the output, you may need to enter these functions in your own CLI instance.

## Import Demonstration Topology

Before we start, please import the demonstration topology.

1. Download [this topology file](../introduction_demonstration.tomato4.json)
2. Open the [topology import page](https://master.tomato-lab.org/topology/import?)
3. Select the topology file you just downloaded, and click on _Import_
4. Select a reasonable topology timeout

You can keep the editor open as you will need this page later

{:.alert .alert-warning}
The editor does not react to changes from outside. You should reload the editor when you have made any changes to the topology with another tool.

## Connect the CLI

Run this command in your console to start the CLI (substitute the hostname if you are using another testbed than the official ToMaTo testbed):
{% highlight shell %}
cd ~/ToMaTo/cli
$ ./tomato.py -h master.tomato-lab.org
{% endhighlight %}

You will be prompted for your username and password. Please enter it.

{:.alert .alert-warning}
When using foreign tools, you must trust its authors when entering your credentials

If you do not get an error message, you have successfully connected to the ToMaTo API.

## Understanding the CLI

The CLI is a Python shell, where all API functions are available as local variables. This means that you can assign variables like this
{% highlight python %}
>>> a = 5
>>> b = 7
>>> a + b
12
{% endhighlight %}

And you can run any API function. For example, you can request information about your account:
{% highlight python %}
>>> account_info()
{% endhighlight %}

Which will return a dictionary containing information about your account.

## Formatting the Output
Dictionaries in Python look untidy if you do not format them properly. To get a nice output, you can run something like this:
{% highlight python %}
>>> import json  # must only be run once in a session
>>> print json.dumps(  account_info()  , indent=2)
{% endhighlight %}

You will see that this output is much easier to read.
Of course, you can use any other function than `account_info()` in this example.

{:.alert .alert-info}
In the following, this tutorial will not use this formatting syntax. Instead, you should use it yourself if you want to print some information.

## A List of Your Topologies

To get a list of your topologies, run `topology_list()`.

## A Note to the Python Shell for Those Who Are Unfamiliar with Python

Lines that require your input start with `>>>` or `...`, while output is printed without such a prompt.

Python differentiates between strings and values, like any usual programming language. However, there is no difference between `""` and `''`; both can mark entire strings.

You may have noticed that this looks like JSON (and we are even using a JSON formatter for better output). You can access certain values of these so-called _dictionaries_. For example, if you want to retrieve only your username, you can use `account_info()["name"]`.
To access certain elements of a list, you can use indexes like you may know from other programming languages' arrays: `topology_list[0]`.

You can iterate over lists with simple for-loops:
{% highlight python %}
>>> for t in topology_list():
...   print t['name']
...
API Tutorial Demonstration
NFV Demo
>>>
{% endhighlight %}

Python doesn't use brackets to combine statements in loops. Instead, it uses indentation.

You can also use variable assignments:
{% highlight python %}
>>> toplist = topology_list()
>>> topology_name = toplist[0]['name']
>>> print topology_name
API Tutorial Demonstration
>>>
{% endhighlight %}

## Getting Fast Help

From the previous commands, you may have understood that the most important functionality is quite easy to understand once you know the basics.

If you are stuck with something, you can use the `help()` command to see a list of available API functions. If you have questions about an API function, you can use the `help(function_name)` (e.g., `help(account_info)`), to see the documentation of the respective function.

{:.alert .alert-info}
If you get an error when trying to see the documentation of a function, it is likely because you have put parenthesis behind the function name.

## Examining the Topology

Most entities can be identified by IDs. These are usually called `id` or `name`. For example, every topology has an `id` attribute, while user accounts have their usernames (`name`).
When you know the identifier of an object, you can request info about it. For example, you can request information about any account by knowing their username. For example, to request information about the account `tutorial`, enter `account_info("tutorial")`.

{:.alert .alert-info}
If you are getting an error, make sure that you are handing the object identifier as a string, not as a variable name.

To get the ID of the topology you recently imported, open the topology editor. You can see the topology ID in the window's URL.
Another way to see IDs is to enable the respective option in the editor's _Options_ tab. This functionality also shows elements' IDs in their right-click menu. IDs in the editor are usually marked by square brackets (`[]`) Try it now!

{:.alert .alert-info}
In most cases, you want to create scripts only for certain topologies. The editor is a great tool for retrieving the ID of elements or connections in complex topologies.

{:.alert .alert-info}
You should use a terminal emulator that supports copy-and-paste. Then, you can simply copy-paste IDs from the editor to the CLI.

So, let's examine this topology in the API: (You need to substitute the topology ID)
{% highlight python %}
>>> print json.dumps(topology_info("58909928a058d400084c4ea4"), indent=2)
{
  "_notes": "This is a demonstration topology for the API tutorial.\n\nIf you have completed this tutorial, you can remove it.", 
  "elements": [
    "58909949a058d400084c4ea5", 
    "5890994aa058d400084c4ea6", 
    "58909950a058d400084c4ea7", 
    "58909950a058d400084c4ea8"
  ], 
  "name": "API Tutorial Demonstration", 
  "state_max": "created", 
  "_initialized": true, 
  "site": null, 
  "connections": [
    "58909950a058d400084c4ea9"
  ], 
  "timeout": 1486130631.217725, 
  "id": "58909928a058d400084c4ea4", 
  "permissions": {
    "tutorial": "owner"
  }
}
>>>
{% endhighlight %}
Let's go through the output line-by-line.

* `_notes` are the topology notes that can be accessed from the editor's _Topology_ tab. The attribute name starts with a `_` because it is client data - Client applications can store any additional value starting with `_` for extended functionality.
* `elements` is a list of element IDs, we will discuss these later.
* `name` is the topology's display name. Note that this is not a unique identifier of your topology.
* `state_max` shows the maximum state of your elements (created < prepared < started)
* `_initialized` is the editor's way to store whether the initialization window (the one that is shown when creating a topology) has to be shown. Again, note that this is client data that has no effect on the functionality behind the API).
* `site` is the site setting in the topology's configuration window.
* `connections` is a list of connection IDs. We will examine this later.
* `timeout` is the topology timeout date. It is a Unix timestamp.
* `id` is the topology's ID
* `permissions` is the users' permission setting.

You see that the topology is basically a collection of elements and connections, and providing access control to these.

You may remember that not only the two devices, but also their network interfaces are elements, which is why there are 4 elements. Let's examine these. But first, we will store the topology info in a variable for easier access.

{:.alert .alert-info}
For all examples that use fixed IDs, these may differ in your setup. Make sure you substitute them in your input.

{% highlight python %}
>>> top_info = topology_info("58909928a058d400084c4ea4")
>>> for element_id in top_info["elements"]:
...   e = element_info(element_id)
...   print e["id"], e["type"], e["name"]
... 
58909949a058d400084c4ea5 openvz Container-Based Debian
5890994aa058d400084c4ea6 kvmqm Full Virtualization Debian
58909950a058d400084c4ea7 openvz_interface eth0
58909950a058d400084c4ea8 kvmqm_interface eth0
>>> 
{% endhighlight %}

This may have been a bit fast, but it should be clear what has happened: We have iterated over the list of element IDs in the topology. For each element ID, we have requested detailed information, and then printed some basic information about this element.

You should be familar with the meanings of `id` and `name`. The `type` attribute defines the element type using easy-to-understand string constants: `full` is a full-virtualization device, and `container_interface` is the network interface of a container-based virtualization device, just to name some examples.

This means that our topology has a container-based and a full virtualization device, as well as one network interface for each of them. This is indeed the case.

At this point, I want to spare you using the CLI for now, since this is a rather unsophisticated tool for browsing detailed information of a topology. It is more useful when you want to actually affect things in your topology. This will be covered in the next tutorial.

All this functionality is also available in the editor. Please enable the _Debug mode_ option in the editor's _Options_ tab.

Now, right-click on the topology and select the _Debug_ entry in the right-click menu. You will see the same information from the API, but in a much more user-friendly interface. Sub-dictionaries and lists are hidden by default, they can be expanded by clicking on them. Please close this now.

{:.alert .alert-info}
You will notice that elements and connections are not only referenced by their IDs, but they are actually included in `topology_info`. To get the same result in the CLI, use `topology_info("58909928a058d400084c4ea4", True)`.

Now, open the _Debug_ window of one of the interface elements. You can see references to a `parent` which is the parent full virtualization device, and a `connection`, which is the connection it is attached to. Additionally, you can see its `name`, its `state`, its `type`, and a reference to its `topology`. There are attributes for `host` and `host_info`, but these are null as long as the element is not prepared. Close this window now.

Open the _Debug_ window of the connection. You will see a list of two elements that are attached to it, its type (connections have a type internally), and its topology. Now, close this window, open its config window, change some link emulation settings, save, and re-open the _Debug_ window. You will se a much bigger list of settings now.
Link emulation can be configured in both directions independently. In the API, this difference is visible in the attribute names that can be `from` and `to`. _From_ references **from the first** to the second element in the `elements` list, and _to_ references from the second **to the first** element.

{:.alert .alert-info}
In many cases, you might wonder how a certain attribute is named exactly, while knowing the attribute. Using the editor to look it up this way can be much faster than using the API reference or the documentation you can access from the CLI.

## Delete the topology

You can delete the demonstration topology now using the editor.

## Exiting the CLI

To exit the cli, press `Ctrl+D` or type `exit()`.


## Conclusion

You have now learned how to 
* Connect to the ToMaTo API
* Run simple API functions
* Use the editor as an information gathering tool while scripting

In the [next tutorial](../first_topology), you will create and start your own topology using the CLI.
