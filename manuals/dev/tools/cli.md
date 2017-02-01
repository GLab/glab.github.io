---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: tools/cli
category: manuals
---

# Command-Line Interface

The Command-line interface (CLI) is an application that can be used to access ToMaTo as a shell, or execute simple scripts as client applications.

## Usage

type `./tomato.py --help` to see a detailed usage specification.

### Testbed Connection

You can use the CLI for any instance of ToMaTo. Thus, you MUST specify a host address.

* `--hostname`, or `-h`: specify host address
* `--port`, or `-p`: specify the port (default: 8000)
* `--protocol`: Protocol to use (default: http+xmlrpc)
* `--ssl`, or `-s`: whether to use ssl (default: not set)

{:.alert .alert-danger}
Keep in mind that most shells store a history of commands. If you provide your password as an argument in a terminal, it may be stored as clear-text in your shell history!

Instead of these three argument, you can use an [API URL](../../api_references#url) instead:

* `--url`, `-u`: URL for the connection.

{:.alert .alert-info}
Internally, the CLI will convert the individual information to a URL to connect.

To connect to the official ToMaTo testbed, run `./tomato.py -h master.tomato-lab.org`

### User Login

Additionally, you can provide user login details. If you do not provide any, you will be prompted to type in missing information:

* `--username`, or `-U`: username
* `--password`, or `-P`: password
* `--keyring`: if set, the CLI will manage your credentials in your system's keyring.


## Shell Mode

Once you have connected and logged in, you see a typical Python shell.

Additionally to default Python functions and statements, you have access to all API functions as global functions, for example:

{% highlight python %}
>>> topology_list()
{% endhighlight %}

### Helper functions

Additionally, you have access to the following helper functions which automatize complex default procedures like the upload and use of images.

[TODO: detailed list]

## Scripts

By default, the CLI will show you a python shell. Instead of this, you can use `--file filename.py` or `-f filename.py` to run a script instead. This script can use the same global API functions as the shell.

