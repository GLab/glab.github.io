---
layout: manual
title: User Manual
manual: setup
manpage: installation
category: manuals
---

# Installation of the ToMaTo Software

To install ToMaTo, simply clone the official git repository:
{% highlight bash %}
$ cd ~
$ git clone https://github.com/GLab/ToMaTo.git
{% endhighlight %}
This will install the software to `~/ToMaTo`.

Now, install the requirements:

{% highlight bash %}
sudo apt-get install python python-ssl docker
{% endhighlight %}

To complete the set-up, you must build the docker containers:

{% highlight bash %}
cd ~/ToMaTo/docker/run
make
{% endhighlight %}

## Updating the Software

You can update the software by fetching the newest commits from git:
{% highlight bash %}
cd ~/ToMaTo
git pull
{% endhighlight %}

You may need to rebuild the docker containers:

{% highlight bash %}
cd ~/ToMaTo/docker/build
make
{% endhighlight %}
