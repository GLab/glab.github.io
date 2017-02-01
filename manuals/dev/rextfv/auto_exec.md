---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: rextfv/auto_exec
category: manuals
---

# Executable Archives: Automatic Execution

Automatic execution happens right after you [upload](../upload) an archive. If your device is in the _prepared_ state upon upload, automatic execution is done right after your device is started.

Automatic execution is the _monitored_ execution of a _start script_. It is monitored so that you can get information whether it is still running or finished, which you can use for further control from the outside.

## <a name="run_status"></a>The run status

The run status is some status information which is created by the _nlXTP monitor_, which is part of the _nlXTP Guest Modules_. [TODO: link to the guest modules] It contains the following values:

* `readable`: bool, whether the `exec_status` directory exists and can be read by the host. All other values are unavailable when this is false.
* `isAlive`: bool, whether the start script's thread is still existing, and whether the nlXTP monitor is alive.
* `done`: bool, set to true when the start script's thread has exited.
* `custom_status`: string, contains [custom information](../custom_status) that can be accessed from outside the device.

Especially the `done` value is useful in order to wait for the execution to be finished.

### <a name="pull"></a>Access to the run status
The values of the run status have to be pulled from your device. To avoid overload, the host updates these values at a certain interval. This interval increases over time, and is reset when executing any action on the respective element.

### Standard Output

You can access the standard and error output of your script at `exec_status/out`. To view this, you may need to [download](../download) the archive directory.

## Writing the start script

The start script can be written in any language, however, bash is preferred. It should start with a shebang (i.e., the first line defining the interpreter, like `#!/bin/bash`).

From the startscript, you have access to the variable `$archive_dir` which contains the path of the archive directory on the device. Additionally, you can use the function `archive_setstatus` which writes all its arguments into the [custom status](../custom_status).

The start script is always executed in the archive directory as working directory.

## Examples

This manual contains many [examples](../../examples/executable_archive) for executable archives.

## API References

[TODO: link] element_info rextfv_run_status
