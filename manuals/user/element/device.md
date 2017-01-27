---
layout: manual
title: User Manual
manual: user
manpage: element/device
category: manuals
---

# Devices

Devices are elements that represent end-hosts. They can also emulate network infrastructure.


## Types

there are three kinds of devices: [container-based virtualization](container), [full virtualization](full), and [Repy](repy). You can distinguish them by their screen color.

### Type selection

If you want to create an element, but are unsure which type to use, answering these questions will help you selecting the device type:

[TODO: insert from wiki]


## Right-Click Menu

The right-click menu highly depend on the device type. These entries are available for all device types:

* [TODO]

Please refer to the individual manual pages for information about more functions.


## Configuration

Configuaration options highly depend on the device type. These options are available for all device types:

* [TODO]

Please refer to the individual manual pages for information about more configuration options.


## Templates and Disk Images

Each device uses its own private [disk image](image). This can be used to store any data, except for Repy devices, where the image is a read-only script.

When preparing a device, the configured [template](../template) will be used as the initial disk image. Templates are the main distinction of devices in the editor's menu and can be configured in the respective configuration menu.

{:.alert .alert-info}
Data on your device is safe unless you [destroy](../../action#destroy) them or [change their template](../../template#change). Note that automatic desctruction can occur due to [topology timeout](../../../topology#timeout).
