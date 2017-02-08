---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: rextfv/custom_status
category: manuals
---

# Executable Archives: Custom Status

The custom status is a field that you can set from inside your element, and access from outside, without using a network connection on your element. The custom status is accessible via the ToMaTo API, making it very easy to access via automated scripts.

## How to set

To set the custom status, you have two options:

* Write the content into `exec_status/custom` in your _archive directory_.
* If you are writing a [start script](../auto_exec), use the function `archive_setstatus`.

## How to access

You can access the custom status from the executable archive information window which can be opened in the editor, or retrieved via `element_info` in the API. Note that the custom status is subject to a [delay](../auto_exec#pull)

## API References

[TODO: link] element_info rextfv_run_status
