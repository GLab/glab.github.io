---
layout: manual
title: User Manual
manual: user
manpage: element
category: manuals
---

# Elements

Elements are the central entities in your topology. They represent [end-hosts](device), [network infrastructure](switch), other elments' [network interfaces](interface), or connectors to [external networks](external_network). In the editor, they are represented by icons with a name below them.

## Element Types

There are different types of elements. Element functionality highly depends on the respective element type, and thus, each of them has its own manual page.

![elements of different types](../img/element_types.png)

* [*Devices*](device) are virtual machines representing end-hosts.
* [*Network Interfaces*](interface) only exist with other elements and represent their network interfaces.
* [*Switches*](switch) represent network infrastructure
* [*External networks*](external_network) are connectors to external networks.

{:.alert .alert-info}
This manual page only covers subjects that apply to all elements. For further information, check the manual pages of the respective element type.

## Creation

You can create non-interface elements by selecting the respective type and configuration form the [editor's menu](../topology/editor#menu).

<video autoplay loop>
	<source src="../vid/element_create.m4v" type="video/mp4">
</video>

## Deletion

Non-interface elements can be deleted via their right-click menu or by using the editor's _Delete_ [mode](../topology/editor#mode).
Elements can only be deleted in the _created_ [state](#state).

{:.alert .alert-info}
Deletion and [destruction](action#destroy) are different things.


## Right-Click Menu

Most interactions with your elements are available in their respective right-click menus. To open it, point your mouse over the target element and press the right mouse button.

![right-click menu](../img/element-rightclick.png)

The right-click menu of an element usually contains the following functions:

* *Connect*: [Connect](#connection) elements
* [*Actions*](action)
* *Resource usage*: [Quota](../account#quota) Quota information
* *Console*: Access to various consoles
* *Disk image*: [Disk image](device/image) functions
* *Executable archive*: [Executable archive](device/executable_archive) functions
* *Configure*: Opens the element's configuration window.
* *Delete*: Delete the element

{:.alert .alert-info}
The available functionalities in the right-click menu differ depending on the type and state of an element.

## Moving Elements

You can move elements in the editor's workspace via Drag & Drop (provided you have selected the respective [mode](../topology/editor#mode) in the editor's home tab). This will not affect your experiment in any way, but it may help you designing the topology.

## <a name="connection"></a>Connections Between Elements

You can create [network connections](../connection) between your elements.

{:.alert .alert-info}
As long as you have not explicitly connected elements to the Internet, there is no network connection between any element and the Internet.

When you create connections between elements, the topology editor will automatically create the respective [interface elements](interface).

{:.alert .alert-info}
You cannot create a connection when one of the to-be-connected elements is in the _started_ state.

## <a name="state"></a>States

Elements can be in different states. The state indicates the current status of deployment on a host. The state is indicated by a small icon at the element.

![element states](../img/element_states.png)

The states are:

* *created*: The element is created in the editor, but not deployed on any host yet.
* *prepared*: The element is deployed on a host, but not running (i.e., the virtual machine is stopped).
* *started*: The element is deployed on a host and running.

{:.alert .alert-info}
Some types of elements do not support the _prepared_ state.

To change the state of an element, you have to run the specific [action](action).

The available element functionality highly depends on its state.


## Configuration Window

Every element has a configuration window which can be accessed via its right-click menu. Please refer to the respective element type's manual page for more information about configuration options. The _help_ button in the top-right corner of the configuration window links to the respective information.

