---
layout: manual
title: User Manual
manual: user
manpage: element/device/executable_archive
category: manuals
---

# Executable Archives

Executable archives provide a unique way to transfer data between your ToMaTo [devices](..) and your local computer, or send commands to your devices without the need to connect your topology to the Internet. This is realized via [RexTFV and nlXTP](/about/publications/2014_A_networkless_data_exchange_and_control_mechanism_for_virtual_testbed_devices_TridentCom.pdf).


## Purpose

Executable archives are good for everything that involves data transfer and the execution of non-interactive commands. Examples:

* Install additional software
* Configure software
* Coordinate the start of software (only via [API](../../../api))
* Get notifications when your experiments have been completed


## How It Works

Archives can be uploaded or downloaded.

Your device has a certain directory, the so-called archive directory.
This directory is the equivalent to your archive. When you upload an archive to the ToMaTo host, it will be extracted so
that it appears in this directory of your device, replacing the old content of the archive directory.
When you want to download an executable archive, the ToMaTo host will create an archive from the contents of this directory.

How the archive directory is realized and possible restrictions are discussed in the pages for the individual types of devices.

### nlXTP guest modules

If the nlXTP guest modules are installed, the following command-and-control interface is available.

If there is a so-called start script with filename `auto_exec.sh` in the root of the archive, this script will be executed automatically after an upload. The status of this script will be constantly monitored by writing certain files into a directory called `exec_status` inside the archive directory. The standard output of the start script will be saved to `exec_status/out` and will be included in an archive download.

It is possible to write custom status information into the file `exec_status/custom_status`. This status can be read and is accessible via the ToMaTo API or the webfrontend.

Please consult the [advanced user's manual](/manuals/dev) for more information about the creation of executable archives, as well as information about the automization of testing with ToMaTo.




## <a name="upload"></a>Uploading an Archive

First of all, you have to create an archive containing all required content. This can be any tar.gz archive.

If you want automatic execution of commands, you have to put a bash script in the root directory of the archive called `auto_exec.sh`.
This script will be executed with the working directory set to the archive directory. In it, you can use the variable `$archive_directory`, which contains its path, and the function `archive_setstatus` which will write all its arguments to the custom status, overwriting the previous one.

You should not include a directory called `exec_status` in your archive.

To upload the archive, make sure your device is in a state where this is supported. Right-click on the device in the editor, open the _Executable Archives_ sub-menu, and select one of the upload options.




### Default Executable Archives

The ToMaTo testbed provides a set of default executable archives. They can be viewed via _Default Executable Archives_ under _Resources_ in the main menu ([→ go now](https://master.tomato-lab.org/web_resources/executable_archive/)). To use them, select _Use a Default Archive_ instead of an upload option and follow the instructions on the screen.

## <a name="download"></a>Downloading an Archive

Archive downloading can save you lots of traffic and time compared to downloading the whole [disk image](../image). You should copy all required data into the archive directory before downloading.

To download the archive, make sure your device is in a state where this is supported. Right-click on the device in the editor, open the _Executable Archives_ sub-menu, and select the download option.

## Execution status

When using a start script, you can see information about its execution, as well as the custom status. To view this, right-click on the device in the editor, open the _Executable Archives_ sub-menu, and select _Status_.

![](../../../img/executable_archive_status.png)

The execution status can also be seen by a small icon next to the element's [state icon](../..#state): This can be a busy icon or a tick.

![busy](../../../img/executable_archive_element_busy.png) ![done](../../../img/executable_archive_element_done.png)
