---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: rextfv/upload
category: manuals
---

# Executable Archives: Upload

The upload of executable archives is the easiest way to transmit data from your computer to a device. The upload is coupled to [automatic execution](../auto_exec), effectively allowing you to send a list of commands together with the data that is uploaded.  

## Building an Executable Archive

The executable archive is a simple .tar.gz archive with any content. However, there is special content attached to the other functionality of executable archives:

* `/auto_exec.sh` is used for [automatic execution](../auto_exec).
* `/exec_status/` is used for monitoring of [automatic execution](../auto_exec) and the [custom status](../custom_status). You should __not__ include such a directory or file in your archive.

## What happens after the upload

First, your content is extracted into the archive directory, removing any previous content. Then, automatic execution is conducted.

## API References

action rextfv_upload_grant and rextrv_upload_use

