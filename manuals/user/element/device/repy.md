---
layout: manual
title: User Manual
manual: user
manpage: element/device/repy
category: manuals
---

# Programmable Devices (Repy)

Programmable devices are essentially scripts that can work with networking packages. These scripts can be written in a Python dialect called _Repy_ and can read and write raw Ethernet packets to/from their network interfaces. Programmable devices are very light-weight as they are just small Python scripts.

Repy is a turing-complete subset of Python that allows to be run in a sandboxed environment.
ToMaTo adds the following functionality to Repy:

 * Reading raw packets from networking devices
 * Writing raw packets to networking devices
 * Listing networking devices and information retrieval
 * Encoding and decoding byte structures using the [struct library](http://docs.python.org/library/struct.html)

### Emulated Virtual Hardware
The only virtual hardware of Programmable Devices are their networking devices. These devices can handle Ethernet packets up to 1514 Bytes.

### Console
For Programmable Devices, the console only displays the output of the script but does not allow any input.

Additionally to the console, this log is also available as a full log for download.

### Images
The Repy scripts of the device can be uploaded and downloaded as [images](../image). A quick sanity check will be performed before the upload.

To learn more about the creation of Repy scripts, consult the [advanced user's manual](/manuals/dev).

### Executable Archives
Executable archives are not supported in Repy devices.

## <a name="config"></a> Configuration Window

### Name

The on-screen name of the device. This setting will not affect your experiment.

### Site

[Site](../../../site_host) that this element will be deployed to.

### Performance Profile

[Device profile](../profile) that will be applied to this element.

### Template

[Template](../template) that will be used when [preparing](../../action#prepare) this element. When your device is [prepared](../..#state), you can still exchange the template.

{:.alert .alert-warning}
Changing the template of a _prepared_ device will delete all existing data on the device's current disk image.

### Segment separation

As long as the _Colorify segments_ option in the topology editor is activated,
ToMaTo highlights separated networks as different segments.
Elements can be defined as connecting elements to combine different network segments.
This does not have any direct effect on the network infrastructure and is **ONLY** for usability purposes.
It allows to mark devices which interconnect networks to increase the overview of the topology.

### Custom Icon

Select a URL to a custom icon for this device to be shown in the editor. The icon should be a 32x32 PNG image.

ToMaTo offers a set of pre-defined custom icons under _Custom Element Icons_ in the main menu's _Resources_ menu. [→ go now](https://master.tomato-lab.org/web_resources/custom_element_icons/)

### Arguments

Arguments that are passed to the script.

## <a name="interface_config"></a> Interfaces' Configuration Window

### Name

The interface's device name on its host (e.g., "eth0")

