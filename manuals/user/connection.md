---
layout: manual
title: User Manual
manual: user
manpage: connection
category: manuals
---

# Connections

Connections are virtual layer-2 network connections between [elements](../element). In the editor, they are represented by a line between the respective elements.

![](../img/connection_example.png)


## Technology and Properties

[TODO]

### Sites

Connections are affected by the properties of the physical connections that they are transported over. Inside a single site, this is not a big problem, but between different sites, this will effect your experiment. However, this means that you can apply real-world properties to your connections.

The connections inside and between sites are constantly measured by ToMaTo. You can see these measurements in the [sites map](insertlink) by clicking on a site, and then selecting the respective link to the target site. For a connection between prepared and started elements, you can see information about the link in the connection's right-click menu by selecting _[TODO: insert correct thing]_

You should carefully select each of your elements' site.


## Create a connection

There are two ways to create a connection:

### Via Connect Mode

1. Select the [_Connect_ Mode](../topology/editor#mode)
2. Click on the first element
3. Click on the second element

<video autoplay loop>
	<source src="../vid/connect_mode.m4v" type="video/mp4">
</video>

### Via Right-Click Menu

1. Right-click on the first element
2. Select _Connect_
3. Click on the second element

<video autoplay loop>
	<source src="../vid/connect_rightclick.m4v" type="video/mp4">
</video>

When you create a connection, the respective [interface elements](../element/interface) are automatically created.


## Right-Click Menu

To open the right-click menu of a connection, click on its _connection handle_. This is the small circle in the middle of the line which represents the connection.

## Delete

To delete a connection, right-click on it and select _Delete_ (or use the _Delete_ mode of the editor). When you delete a connection, the editor automatically deletes the respective interface elements.


## Configuration Options

You can configure [link emulation](link_emulation) and [packet capturing](packet_capturing) on connections.
