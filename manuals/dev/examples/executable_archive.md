---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: examples/executable_archive
category: manuals
---

# Examples: Executable Archives

This page contains a number of example executable archives. Some archives contain links too.

## Software Installer

This is a very simple example: you have a debian package, `toinstall.deb`, and two dependencies, `dep1.deb` and `dep2.deb`, and you want to install them on a target element.

This can be easily achieved. First, you create a start script containing the following content:
{% highlight bash %}
#!/bin/bash
dpkg -i *.deb
{% endhighlight %}
and your executable archive's file structure looks like this:
{% highlight bash %}
.
|
+-- toinstall.deb
+-- dep1.deb
+-- dep2.deb
+-- auto_exec.sh
{% endhighlight %}

## <a name="autoconfig"></a>Automatic Configuration

In this example, you have two executables: `client` and `server`. You want to install both to `/testsoftware`, and run a script called `/start` which will automatically start the correct software. Whether this is the server or client application is determined by the element's hostname, which can be set in container-based elements' configuration windows.

Your `auto_exec.sh` script should like this:
{% highlight bash %}
#!/bin/bash
mkdir /testsoftware
cp client /testsoftware
cp server /testsoftware
cp start /
{% endhighlight %}

and your `start` script contains the following:
{% highlight bash %}
#!/bin/bash
cd /testsoftware

# if component is given as argument, use this. Otherwise, try to guess it from the hostname.
if [ $# -eq 0 ]; then
	component=$(hostname | awk '{print tolower($0)}')
else
	component=$1
fi

case $component in
	server)
		./server serve
		exit
		;;
	client)
		./client
		exit
		;;
	*)
		echo "bad component: ${component}"
		exit 1
		;;
esac
{% endhighlight %}

Your executable archive includes the software, `start` and `auto_exec.sh` in its root directory.

## Experiment Start

By precisely timing the `rextfv_upload_use` actions, you can start your experiment.
Let's assume you have uploaded and executed the script from the [Automatic Configuration](#autoconfig) example, and now you want to start both components.

You can do this by uploading an executable archive containing only a `auto_exec.sh` script with this content:
{% highlight bash %}
#!/bin/bash
cd /
./start
{% endhighlight %}

Instead of relying on automatic configuration, you can of course send any other command this way, for example:

{% highlight bash %}
#!/bin/bash
cd /testsoftware
./server serve
{% endhighlight %}

This is an easy example how you can transmit commands without any payload.

[TODO: example that does this as a script: complete experiment setup]

## Packet Finder

This is a simple version of the [packet manager](/manuals/dev/tools/getpackages): this script should give us a list of packages to be installed, and their URLs. In order to do this, this will be uploaded to a Debian element which is connected to the Internet.

To do this, you can use a start script which reads the to-be-installed packets from a file called `toinstall` in the archive directory:
{% highlight bash %}
#!/bin/bash
toinstall = $(cat $archive_dir/toinstall)
apt-get update
archive_setstatus "$(apt-get --print-uris -y -qq install --no-install-recommends $toinstall)"
{% endhighlight %}

The archive contains both `toinstall` and `auto_exec.sh` in its root directory.

After executing, this script will return a list of URLs and filenames in the custom status.

[TODO: example that uses this to create an archive like the first one]

