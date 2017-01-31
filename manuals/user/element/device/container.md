---
layout: manual
title: User Manual
manual: user
manpage: element/device/container
category: manuals
---

# Container-Based Devices

Container-based virtual devices are light-weight virtual machines that translate kernel calls to kernel calls of the host kernel. Container-based virtualization technologies offer complete usermode access to the virtual machines and a limited kernel-mode access. The kernel mode access allows to:

  * Manage networking hardware
  * Use raw sockets

### Limitations
  * Only Linux
  * No kernel modules
  * No kernel changes
  * No NFS mounting
  * No graphical hardware, and thus no desktop environment possible

### Console
The console access is realized as a shell inside the virtual machine. The access is comparable to an ssh session. Multiple concurrent windows will show the same console but when all windows showing the console are closed, the console will be terminated and the next window will show a new clean console. This has several implications:
* The console does not require any login. This does not mean that the system is insecure, the ssh server will prompt for a login as normal.
* The console is text-based, so no graphical programs can be executed.
* The meaning of pressed keys depends on the keyboard layout of the real keyboard of the user.

### Images
The root file-system is stored in a folder on the host machine. The file-system can be download and uploaded as a tar archive compressed with gzip (.tgz or .tar.gz). When extracting or creating such an [image](../image), keep in mind that file ownership can only be set properly if the user has root permissions and all the users and groups in the image exist. When this is not done properly the resulting compressed archive will not be bootable.

To learn more about the creation of images, consult the [developer's manual](/manuals/dev).

### Executable Archives

Executable archives can be uploaded and downloaded when the device is _prepared_ or _started_. Automatic execution is possible only when [nlXTP guest modules](../image#nlXTP) are installed on the image.

The archive directory is part of the device's image. It can be found at `/mnt/nlXTP`

### Technologies
ToMaTo supports the following technologies for container-based virtualization:
* LXC (preferred)
* OpenVZ

## <a name="config"></a> Configuration Window

### Name

The on-screen name of the device. This setting will not affect your experiment.

### Site

[Site](../../../site_host) that this element will be deployed to.

### Performance Profile

[Device profile](../profile) that will applied to this element.

### Template

[Template](../template) that will be used when [preparing](../../action#prepare) this element. When your device is [prepared](../..#state), you can exchange the template.

{:.alert .alert-warning}
Changing the template of a _prepared_ device will delete all existing data on the device's current disk image.

### Segment separation

[TODO]

### Custom Icon

Select a URL to a custom icon for this device to be shown in the editor. The icon should be a 32x32 PNG image.

ToMaTo offers a set of pre-defined custom icons under _Custom Element Icons_ in the main menu's _Resources_ menu. [→ go now](https://master.tomato-lab.org/web_resources/custom_element_icons/)

### Hostname

The device's hostname (as in /etc/hostname)

### IPv6 gateway and IPv4 gateway

IP gateway configuration for your device

### Root password

The device's root password.

## <a name="interface_config"></a> Interfaces' Configuration Window

### Name

The interface's device name on its host (e.g., "eth0")

### IPv4 address

The interface's IPv4 address and subnet (e.g., "10.0.0.1/24")

### Use DHCP

Use DHCP instead of the configured address

### IPv6 address

The interface's IPv6 address

