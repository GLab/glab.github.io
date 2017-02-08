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

There are three kinds of devices: [Container-based virtualization](container), [full virtualization](full), and [Repy](repy). You can distinguish them by their screen color.

### Type selection

If you want to create an element, but are unsure which type to use, answering these questions will help you select the device type:

On the first look, full virtualization seems to be the better choice as it allows more operating systems and does not limit operating system functionality. Container-based virtualization though, is a very light-weight solution that gives quick access to Linux machines and is much easier to handle than full virtualization. E.g. Container-based virtualization allows users to configure theroot password or the IP addresses of the interfaces. Additionally, full virtualization consumes a lot of resources on the testbed, so it should be avoided if it is not necessary.

This list of criteria can help with the choice:


{:.table .table-bordered}
| Criteria | Recommendation |
|---------|--------------|
| Do you need realtime functionality or extremely precise timing? | Use a Physical system (not supported by ToMaTo) |
| Do you need to run hardware virtualization inside the device? | Use a physical system |
| Do you want to test your own low-level protocol? | Use Programmable Devices |
| Do you want to apply simple modifications to packets? | Use Programmable Device |
| Do you need an operating system other than Linux? | Use full virtualization |
| Do you need to access the hardware? | Use full virtualization |
| Do you need to modify the kernel or load modules? | Use full virtualization |
| Do you need to setup routing tables, iptables or mount filesystems? | Use full virtualization |
| Otherwise | Use container-based virtualization |

## Configuration

Configuration options highly depend on the device type. Please refer to the individual manual pages ([Container](container#config), [Full](full#config), [Repy](repy#config)) for information about configuration options.


## Templates and Disk Images

Each device uses its own private [disk image](image). This can be used to store any data, except for Repy devices, where the image is a read-only script.

When preparing a device, the configured [template](../template) will be used as the initial disk image. Templates are the main distinction of devices in the editor's menu and can be configured in the respective configuration menu.

{:.alert .alert-info}
Data on your device is safe unless you [destroy](../../action#destroy) them or [change their template](../../template#change). Note that automatic destruction can occur due to [topology timeout](../../../topology#timeout).
