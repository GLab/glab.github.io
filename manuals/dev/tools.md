---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: api_tutorial
category: manuals
---

# Tools

ToMaTo provides a set of tools to access it or to create resources with it.

## Installation

There is currently no distributed package for installing the ToMaTo tools. Thus, you have to clone them manually.

By now, only Linux is supported.

First, you should install the dependencies:
{% highlight shell %}
$ sudo apt-get install python git
{% endhighlight %}

Then, you can clone the [official GitHub repository](https://github.com/GLab/ToMaTo):
{% highlight shell %}
cd ~
git clone https://github.com/GLab/ToMaTo.git
{% endhighlight %}

The tools will then be located at `~/ToMaTo/cli`. You may choose a different location, but you might need to change the paths in this directory accordingly.

{:.alert .alert-info}
If you see any command like `./tomato.py` in this manual, you will most likely find it in the `~/ToMaTo/cli` directory.

## Command-Line Interface

The [command-line interface](cli) (CLI) is a tool which can be used to directly use the API in a python shell, or to execute simple API scripts.

## Executable Archive Packet Manager

The [executable archive packet manager](getpackages) is a sophisticated tool to create executable archives for installing additional OS software.

