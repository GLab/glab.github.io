---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: rextfv/download
category: manuals
---

# Executable Archives: Download

You can download the entire _archive directory_ of an element. The result of this is a tar.gz archive.

This functionality avoids transmitting the whole disk image, which may be rather large, especially if you are only interested in some experiment results. Moreover, this functionality is available while your device is started. Also, a disk image does not necessarily include the archive directory.

The download also contains the `exec_status` directory, which contains all output of your executed scripts and all data your scripts stored there for evaluation purposes. 

## API References

[TODO: link] action rextfv_download_grant

