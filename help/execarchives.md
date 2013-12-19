---
layout: default
title: Executable Archives
category: help
---
# Executable Archives

## Introduction
An executable archive is an easy way to transmit data or execute scripts.

## Structure
An executable archive is a .tar.gz file.

Every device has an nlXTP-directory (usually located at /mnt/nlXTP).
When uploading an archive, the contents of this directory are overwritten.
When downloading an archive, the downloaded file contains this directory.

After uploading, if the archive

* contains a script matching auto_exec.sh in its root and
* does not contain a directory called exec_status in its root,

the script will be executed (note: the script should start with a shebang line.).
The output of this execution will be saved at exec_status/out inside the nlXTP directory.
Status information are available for this execution.

If the device is not started while uploading, the execution will be delayed until the device will be started the next time.


## Use cases
An executable archive can transmit data or execute commands.
It can also execute operations on the transmitted data, so it can be viewed as a function with attached resources.


## Guest modules
Main article: [Guest Modules]()

For executable archives to work properly, the devices must be configured.

On KVM devices, the nlXTP directory is a floppy disk which must be mounted on the right place.
On OpenVZ devices, no mount configuration is necessary to access the uploaded data.

Auto-execution and execution status are only available iff the guest modules are installed.
However, the directory is still available (upload and download) without guest modules.

## Guest Functions
The guest modules come with guest functions and variables to make interacting with archives easier for users.

### Custom Status (since version 0.3)
It is possible to set a user-specified String as status. 
This status can be used for scripting purposes. If it is properly formatted, an interpreter can read it as it is written.
It can also be accessed by the web in the archive execution status window.

To set a custom status, use the guest function "archive_setstatus". This is a bash command which takes any number of argument and writes them as the new status.

### Guest module version (since version 0.3)
If you need to know the guest modules version, use the variable "archive_version".
This variable contains the current version.
