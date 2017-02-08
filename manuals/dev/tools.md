---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: tools
category: manuals
---

# Tools

ToMaTo provides a set of tools to access it or to create resources with it.

## Installation

There is currently no distributed package for installing the ToMaTo tools. Thus, you have to clone them manually.

By now, only Linux is supported.

First, you should install the dependencies:
{% highlight shell %}
$ sudo apt-get install python python-openssl git
{% endhighlight %}

Then, you can clone the [official GitHub repository](https://github.com/GLab/ToMaTo):
{% highlight shell %}
$ cd ~
$ git clone https://github.com/GLab/ToMaTo.git
{% endhighlight %}

The tools will then be located at `~/ToMaTo/cli`. You may choose a different location, but you might need to change the paths in this directory accordingly.

{:.alert .alert-info}
If you see any command like `./tomato.py` in this manual, you will most likely find it in the `~/ToMaTo/cli` directory.

## Command-Line Interface

The [command-line interface](cli) (CLI) is a tool which can be used to directly use the API in a python shell, or to execute simple API scripts.

## ToMaTo Library

The [ToMaTo library](lib) contains methods for connecting to the API and simplifying certain procedures.

## Executable Archive Packet Manager

The [executable archive packet manager](getpackages) is a sophisticated tool to create executable archives for installing additional OS software.

## Template Migration Script

The template migration script is a script which connects to two ToMaTo testbeds at once in order to copy a set of templates from one testbed to another. This is heavily used for internal test setups, but can also be used by testbed administrators to synchronize resources of their own ToMaTo instance to another one.

The template migration script is a command-line tool called `migrate_templates.py`. Type `--help` to get more information about its usage.

Its syntax is similar to that of the CLI, with a few differences:

* It supports two testbed connections at once: a source and a destination.
  * the respective arguments for the connections have been renamed to reflect this difference: For example, use `-sh` or `-dh`, respectively, where you would use `-h` at the CLI (`--host_source` or `--host_destination`, respectively).
  * Templates will be transmitted from source to destination.
* Use `--templates` as last argument, followed by a space-separated list of template names.
  * If you do not provide this, all templates will be copied!
* By default, all restricted templates will be skipped.
  * The `--include_restricted` argument can be set to include restricted templates.
* By default, if a template already exist on the destination testbed, it will be skipped.
  * Use `--overwrite_on_conflict` to overwrite existing templates.

## Backend Registrator

The backend registrator is a tool which can automatically register a backend's public key on a target host. In order for this to work, the user must have a login to the target testbed and SSH access to the host.

The script is named `register_backend_on_host.sh`. You need to use a [URL](../api_references/#url) for the backend connection. The usage is: `./register_backend_on_host.sh BACKEND_URL HOST_ADDRESS CERT_IDENTIFIER`, e.g., `./register_backend_on_host.sh http+xmlrpc://master.tomato-lab.org 131.246.112.36 example_testbed`

* BACKEND_URL: URL to the backend API
* HOST_ADDRESS: IP address or domain name for the target host
* CERT_IDENTIFIER: identifier for the backend cert on the host (any string meaningful to host administrators)

