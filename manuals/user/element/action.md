---
layout: manual
title: User Manual
manual: user
manpage: element/action
category: manuals
---

# Actions

Actions are heavy-weight functions that run exclusively on the respective [element](..). They have a high impact on their target and may take several minutes to finish.

## State Actions

State actions are used to manipulate the [state](..#state) of their target. They can be executed by selecting the respective entry in the target element's right-click menu, or by conducting topology actions. Topology actions conduct the respective action on all suitable elements simultaneously.

{:.alert .alert-info}
[Interface elements](../interface) do not accept actions: their state is changed automatically with their associated parent element.

State actions are only available when the respective element is in the respective starting state.

### <a name="prepare"></a>prepare

The _prepare_ action leads an element from the _created_ state to the _prepared_ state.

First, a suitable host is selected for the element by the _load balancer_. Then, all required information about the element is sent to the target host, where the element is then prepared.

### <a name="start"></a>start

The _start_ action leads an element from the _prepared_ or _created_ state to the _started_ state.

If the element supports the _prepared_ state and is in _created_ state, the functionality of the _prepare_ action will be conducted automatically before starting.

### <a name="stop"></a>stop

The _stop_ action leads an element from the _started_ state to the _prepared_ state.

### <a name="destroy"></a>destroy

The _destroy_ action leads an element from the _prepared_ or _started_ state to the _created_ state.

This means that the element is removed from the host, and all data associated with it is deleted.


## Other Actions

There is other functionality which is implemented as actions. For example, changing a [template](../template) or using [executable archives](../device/executable_archive). However, this has no impact on the user of a webfrontend. If you are interested in more information, consult the [advanced user's manual](/manuals/dev).
