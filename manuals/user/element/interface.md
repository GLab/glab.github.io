---
layout: manual
title: User Manual
manual: user
manpage: element/interface
category: manuals
---

# Interface Elements

Interface elements are special elements that are attached to other elements and represent their inidividual network interfaces. They form a child-parent relationship with their parent elements.

## Creation and Deletion

The editor automatically creates and deletes interface elements with their respective [connection](../../connection). Interface elements are also deleted with their parent element.


## Interaction

Interface elements are represented by small circles around their parent elements. Note that you can interact with them via their right-click menu like you can interact with any other elements.

![](../../img/connection_example.png)

{:.alert .alert-info}
If the interface is not visible on your connections, make sure that _Connection Controls_ are enabled in the editor's _Options_ Menu tab.

## Right-Click Menu

* *Resource usage*: Information about the interface's [quota](../../account#quota) usage.
* *Configure*: Opens the config window.
* *Delete*: Delete the interface, and its connection.

## Actions

Interface elements do not support [actions](../action) themselves. They change their [states](..#state) automatically with their parents.

## Configuration

Configuration options highly depend on the device type of the parent device. Please refer to the specific manual page ([Container](../device/container#interface_config), [Full](../device/full#interface_config), [Repy](../device/repy#interface_config)) for more information.
