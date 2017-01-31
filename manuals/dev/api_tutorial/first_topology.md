---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: api_tutorial/first_topology
category: manuals
---

# API Tutorial: First Toplogy

Welcome to the second API tutorial. In this tutorial, you will use the cli to create your first topology, populate it with elements and a connection, start it, access the console, and then tear it down.

Please connect a CLI to the API in order to continue.

## Create your topology

Creating a topology is easy: simply run
{% highlight python %}
>>> topology_create()
{'elements': [], 'name': 'Topology [5890afcfa058d400084c4eb6]', 'state_max': 'created', 'site': None, 'connections': [], 'timeout': 1485880799.048256, 'id': '5890afcfa058d400084c4eb6', 'permissions': {'tutorial': 'owner'}}
>>>
{% endhighlight %}
The return value of `topology_create` is the topology info of the new topology.

{:.alert .alert-warning}
Not all functions in the ToMaTo API are idempotent. When executing an API call, think about its effects first!

Oh no! You forgot to store the result of this API call in a variable! - No problem, the result of the last call can always be accessed as `_`:
{% highlight python %}
>>> topology_create()
{'elements': [], 'name': 'Topology [5890afcfa058d400084c4eb6]', 'state_max': 'created', 'site': None, 'connections': [], 'timeout': 1485880799.048256, 'id': '5890afcfa058d400084c4eb6', 'permissions': {'tutorial': 'owner'}}
>>> top_id = _['id']
{% endhighlight %}

We will need the topology ID very often, this is why we store it here. Note that new topologies are initialized with a timeout of one hour. We don't want to learn while having time preasure, so we should increase the timeout. Renewing a topology is an action.

{% highlight python %}
>>> topology_action(top_id, "renew", {"timeout": 2*24*60*60})
{% endhighlight %}

This will set the topology timeout to two days in the future.

{:.alert .alert-info}
The syntax for actions is always the same. The functions `topology_action` and `element_action` take the arguments `(id, action_name, kwargs)` where `action_name` is a string constant, and `kwargs` is a dictionary.

We should assign a nice name to the topology, so that it will have a meaningful name in the topology list.

{% highlight python %}
>>> topology_modify(top_id, {"name": "First CLI-Created Topology"})
{% endhighlight %}

This looks way better.

{:.alert .alert-info}
The syntax for modify functions is alwas the same. The functions `topology_modify`, `element_modify`, `account_modify` and so on take two arguments, the first being the id of the identity that should be modified, and the second being a dictionary. This dictionary only contains the attributes that should be changed.

## Creating Elements

Our topology is empty, so we should now create two devices. We shall create two container-based devices with the default template.
{% highlight python %}
>>> el1_id = element_create(top_id, "container", None, {"name": "el1"})["id"]
>>> el2_id = element_create(top_id, "container", None, {"name": "el2"})["id"]
{% endhighlight %}

{:.alert .alert-info}
`create` functions usually return the created entity's info. Also, most `create` functions accept an optional `args` argument, which has the same functionality as in the `modify` function.

{:.alert .alert-info}
The newly created elements do not have positions in the workspace assigned to them. When you open the topology, the editor will randomly set positions. You can use the `_pos` attribute to select positions: It is a dict containing two coordinates, each is a float between 0 and 1.


## Connecting the Elements

Now, we should connect these elements. While the editor automatically creates interfaces for us, we have to do this manually here.
{% highlight python %}
>>> el1_if_id = element_create(top_id, "container_interface", el1_id)["id"]
>>> el2_if_id = element_create(top_id, "container_interface", el2_id)["id"]
{% endhighlight %}

Then, we can connect the two interfaces:
{% highlight python %}
>>> con_id = connection_create(el1_if_id, el2_if_id)["id"]
{% endhighlight %}

We don't need to pass the topology ID to `connection_create` as the topology is already defined by the elements. You cannot connect elements from different topologies.


## Starting the Topology

We can use the topology start action to start the whole topology:

{% highlight python %}
>>> topology_action(top_id, "start")
{% endhighlight %}

This function call will block until everything is started.


## Accessing the Elements

You can use the editor to access the devices' console to see for yourself that the devices are properly connected to each other.

Using `ifconfig` you may notice that our devices do not have IP addresses assigned to them. We simply forgot this. Luckily, we can do this while the devices are running:
{% highlight python %}
>>> element_modify(el1_if_id, {"ipv4address": "10.0.0.1/24"})
>>> element_modify(el2_if_id, {"ipv4address": "10.0.0.2/24"})
{% endhighlight %}

Now, we can run a ping test between the devices.


## Removing the Topology

{:.alert .alert-danger}
Old topologies that are still running waste a huge amount of resources. Be fair and clean up after your experiments.

We should now stop and remove our topology.
{% highlight python %}
>>> element_action(el1_id, "stop")
>>> element_action(el2_id, "stop")
>>> element_action(el1_id, "destroy")
>>> element_action(el2_id, "destroy")
{% endhighlight %}

{:.alert .alert-info}
You can simply run `topology_action(top_id, "destroy")` instead of doing this manually. This was just for demonstration purposes.

{% highlight python %}
>>> topology_remove(top_id)
{% endhighlight %}

{:.alert alert-info}
`element_remove` and `topology_remove` will recursively remove all child elements and connections.

## Conclusion

You have now learned how to use the API to conduct experiments. 

By now, you should have understood the meaning and basic syntax of the different `_create`, `_info`, `_modify`, `_action`, and `_remove` functions.

