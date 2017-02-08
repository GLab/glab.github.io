---
layout: manual
title: User Manual
manual: user
manpage: topology/editor
category: manuals
---

# Topology Editor

The topology editor is a graphical web-based tool to design and control your topology. It is the only way to access topologies in the webfrontend.

{:.alert .alert-info}
You must enable JavaScript for the editor to work.

The editor consists of two main parts: The _menu_ and the _workspace_:
![editor overview](../../img/editor_overview.png)


## <a name="menu"></a>The Menu

The menu allows you to control the topology and add new [elements](../../element) to it. It consists of five main tabs, each of which will be discussed here:

### Home

The home tab contains the mostly used tools:

![](../../img/editor-home-tab.png)

* <a name="mode"></a>*Modes* selects the mode. This is important since this defines what a left-click will do in the workspace. One of these tools is always active. You can see which mode is active either on these buttons, or on your cursor when hovering over an element.
  * _Select & Move_: This tool allows you to move elements via drag&drop on the workspace.
  * _Connect_: This tool allows you to connect elements. When the tool is active, click on one element and then on a second one to connect them. To cancel the operation after the first click, click on the same element again.
  * _Delete_: This will delete elements with one click. Caution!
* *Topology control* contains the most important element [actions](../../element/action). These actions will be conducted on all elements where it is possible.
* *Common elements* contains the most important elements from the _Devices_ and _Network_ tabs.

### Devices

![](../../img/editor-devices-tab.png)

The devices tab contains most [templates](../../element/template) for [device elements](../../element/device). You can add a device to your topology by clicking on one of the buttons there, and then clicking on the target position on the workspace.

There are special _Upload own image_ devices. These are devices which will be prepared directly, and you will be prompted to [upload your own custom image](../../elememt/image) directly.

### Network

![](../../img/editor-network-tab.png)

The network tab contains the remaining devices, as well as [external networks](../../element/external_network).

### Topology

The topology tab contains topology control functions:

![](../../img/editor-topology-tab.png)

* *Consoles (NoVNC)* opens a window containing all consoles of all devices.
* *Notes* opens a window where users can add notes. The notes window can be configured to automatically open when loading the editor.
* *Resource usage* shows [quota](../../account#quota) statistics for the topology.
* *Renew* allows you to renew your topology to avoid a [topology timeout](..#timeout)
* *Rename* allows you to change the name of your topology
* *Export* can [export](..#export) your topology
* *Delete* will remove your topology.
* *Users & Permissions* opens the [permissions window](../permission).

{:.alert .alert-danger}
Note that *Delete* will [destroy](../../element/action#destroy) all elements in a topology, meaning you will lose all respective data!

### Options

The options tab contains multiple options that change the editor's behavior:

![](../../img/editor-options-tab.png)

* *Topology* are topology-specific settings which are synchronized between all its users.
* *User* contains user-specific settings which are synchronized between all topologies, but different for each user.

The options are in detail:

* _Safe mode_: Ask before performing destructive actions (stop, destroy, remove)
* _Snap to grid_: Elements will use a grid for positioning - this creates a more ordered topology
* _Fixed positions_: Prevents the user from moving elements
* _Big workspace_: Increases the size of the workspace. The distances between elements will be adapted when resizing. This requires a reload of the topology.
* _Colorify segments_: Colorify connections based on network segments
* _Show IDs_: Show element and connection IDs in their right-click menus. This is useful when accessing the topology from the [API](../../api).
* _Show element sites_: Show elements' sites in their right-click menu.
* _Debug mode_: Show a _debug_ menu entry in every right-click menu which grants access to the [API](../api) info result. Useful when accessing the topology from the API.
* _Show connection controls_: Show interface elements and the connection handle. This should always be active, but disabling it will result in better-looking screenshots.

{:.alert .alert-warning}
Although topologies can be shared between users, the editor should not be used by multiple users at once when modifying a topology or running [element actions](../../element/action).


## The Workspace

The workspace is the place where you design your topology. It shows elements and their connections. Please refer to the individual manual pages to learn how to control and manipulate elements and connections.


### Topology Right-Click Menu

When you right-click on any white space in the topology, you can open a right-click menu which gives you quick access to the most important functions from the menu.

![](../../img/topology-rightclick.png)



