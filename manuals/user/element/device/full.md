---
layout: manual
title: User Manual
manual: user
manpage: element/device/full
category: manuals
---

# Full Virtualization Devices

Full virtualization devices are heavy-weight virtual machines that emulate a whole computer with generic hardware. Most things that are possible on physical computers is also possible on fully virtualized devices. Most operating systems can be run on KVM. 

### Limitations
  * Virtualization solutions might not work. Since the virtual machine itself is virtualized it does not expose the AMD-V/VT-x processor features to the guest operating system.
  * The hardware clock runs on GMT time zone. This will be a problem with Microsoft operating systems since they assume the hardware clock to be local time.
  * Timer precision will not be as high as on real hardware since the virtual machine's process is scheduled by the host system.

### Emulated Hardware
* Processor and RAM depending on the performance profile
* One hard-disk connected to the first IDE as master
* Intel motherboard
* Cirrus Logic GD5446 Video card
* Intel E1000 network cards
* PS/2 mouse and keyboard (german layout)
* Additionally a USB tablet input device (for absolute mouse positioning)

The emulated environment is the same as in KVM run with: ```kvm -cpu kvm64 -usbdevice tablet -smp sockets=1,cores=1 -nodefaults -vga cirrus -tdf -k de -enable-kvm  -net nic,model=e1000 ...```

### Console
The console access is realized as vnc connection to the graphics output. The console will show exactly the output of the graphics card of the virtual machine. Keyboard or mouse events will be sent to the server via its emulated keyboad and mouse devices. This has several implications:
* The console is not text-based even if a text-based console is displayed.
* Multiple console windows will show the same console.
* The meaning of pressed keys depends on the keyboard layout configured for the emulated virtual keyboard in the virtual machine, not on the real keyboard of the user.
* Closing the console is the same as disconnecting the monitor cable from a computer (emulated keyboard and mouse are not disconnected)

### Images
The hard-disk [images](../image) are stored in the qcow2 format. When they are downloaded they can be run in Qemu. Disk images in the qcow2 format can be uploaded and run. For operating systems that have problems with hardware changes, qemu should be configured to emulate the same hardware as in the testbed.

To learn more about the creation of images, consult the [developer's manual](/manuals/dev).

### Technologies
ToMaTo supports the following technologies for full virtualization:
* KVM (preferred) (in stable, but not deployed)
* KVMQM

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

### USB tablet mouse mode

[TODO]

### Keyboard Language

[TODO]

## <a name="interface_config"></a> Interfaces' Configuration Window

### Name

The interface's device name on its host (e.g., "eth0")

