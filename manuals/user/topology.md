---
layout: manual
title: User Manual
manual: user
manpage: topology
category: manuals
---

# Topologies

Topologies are the basic entities in ToMaTo. A topology represents a complete network topology including [end-host devices](../element/device), [routers and switches](../element/switch), and [connections](../connection) between them.

{:.alert .alert-info}
As long as you have not explicitly connected elements to the Internet, there is no network connection between any element and the Internet.

You can create multiple topologies, each of which will be separated from each other. Usually, you will create one topology per experiment.


## Access

To see a list of available topologies, click on "My Topologies" in the main menu. [→ go now](https://master.tomato-lab.org/topology)

In the list of available topologies, you can select an existing topology, or create a new one. When doing so, the [topology editor](editor) will open, providing you with full control over the topology. 


## Permissions

Topologies can be shared between multiple users. Read more about this [here](permission).


## <a name="timeout"></a>Timeouts

Topologies time out after a while. This avoids old topologies from being forgotten and never stopped. In order to use your topologies for a long time, you must _renew_ them regularly. This can be done in the editor via the _Renew_ button in the _Topology_ tab.

When the topology reaches its timeout, all elements will be [stopped](../element/action#stop). A long time after the timeout, the elements will be [destroyed](../element/action#destroy). Some time after the destruction, the topology will be removed.


## Tutorials

ToMaTo provides tutorials for new users. These tutorials can also be accessed from the topology list page. [→ go now](https://master.tomato-lab.org/tutorial)

It is possible to load third-party tutorials which can also be used for educational purposes. Consult the [advanced user's manual](/manuals/dev) to learn how to write your own tutorials.


## <a name="export"></a>Export and Import

You can export your topology design to a file by clicking on the _Export_ button in the editor's _Topology_ tab. This will export only the data that would be left in the [created](../element#state) state, i.e., what is left after destruction.

You can import the exported file on the topology list page.


## Remove

You can remove the topology via the editor by clicking on the _Delete_ button in the _Topology_ tab.

{:.alert .alert-danger}
Removing a topology will [destroy](../element/action#destroy) all elements of this topology, hence removing all respective data belonging to these elements from the system!