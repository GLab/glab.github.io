---
layout: manual
title: User Manual
manual: user
manpage: element/device/image
category: manuals
---

# Disk Images

Each device uses its own private disk image. This can be used to store any data, except for Repy devices, where the image is a read-only script.

To understand what data the disk image contains, please refer to the respective device type's manual page.

{:.alert .alert-info}
Data on your device is safe unless you [destroy](../../action#destroy) them or [change their template](../../template#change). Note that automatic desctruction can occur due to [topology timeout](../../../topology#timeout).


## Templates

When preparing a device, the configured [template](../../template) will be used as the initial disk image. Templates are the main distinction of devices in the editor's menu and can be configured in the respective configuration menu.


### Change template

{:.alert .alert-warning}
Changing the template of a _prepared_ device will delete all existing data on the device's current disk image.

You can replace your current disk image with any template while the element is in the _prepared_ state. You can do this by either changing it in the device's config menu, or by right-clicking on the target element, open the _Disk Image_ submenu, and select _Change template_.


## Download Data

{:.alert .alert-info}
If you just want to download experiment results, you should consider to [download an executable archive](../executable_archive#download) instead.

You can download a device's disk image in its _prepared_ state. To do this, right-click on the target element, open the _Disk Image_ submenu, and select _Download image_.


## Upload your own disk image

{:.alert .alert-info}
If you just want to install software, you should consider to [upload an executable archive](../executable_archive#upload) instead.

You can upload your own custom disk images. To do this, right-click on the target element, open the _Disk Image_ submenu, and select one of the upload options.


