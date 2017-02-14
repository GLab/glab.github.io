---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: tools/lib
category: manuals
---

# ToMaTo Library

The ToMaTo library grants you access to the ToMaTo API as well as some special functionality in your own, independent Python app.

## Preparation

We assume you already have started developing your own Python app. This means that there is a root module with multiple sub-modules. The folder structure may be something like this:
{% highlight bash %}
~/myapp/
│
├── somelib/
│   └── __init__.py
├── __init__.py
└── somefile.py
{% endhighlight %}

Furthermore, it is assumed that you have cloned the git repository to `~/ToMaTo`.

## Include the Library

The library is available at `~/ToMaTo/cli/lib`. In order to add it to your project, you have multiple possibilities:

### The Symbolic Link Method

You can use a symbolic link from your project to the repository.

{% highlight bash %}
cd ~/myapp
ln -s ~/ToMaTo/cli/lib tomato_lib
{% endhighlight %}

{% highlight python %}
import tomato_lib
{% endhighlight %}

Pro: The library can be updated by fetching the newest updates from the repository.

Con: This solution is not portable, or requires additional set-up when copying your project to a new computer.

### The Copy Method

Instead of using a symlink, you can copy the ToMaTo library to your project:

{% highlight bash %}
cd ~/myapp
cp -rL ~/ToMaTo/cli/lib tomato_lib  # you can use a relative path instead
{% endhighlight %}

{% highlight python %}
import tomato_lib
{% endhighlight %}

Pro: Creates a portable app

Con: Updating the ToMaTo library requires an update of the copies after updating the repository.

{:.alert .alert-danger}
There are repository-internal, relative symlinks in the library itself. Double-check that you don't have symlinks in your local copy!

### The PATH Method

Instead of using a symlinc, you can add the respective directory to your app's path. This can be achieved by running

{% highlight python %}
import sys
sys.path.insert(1, "/home/yourusername/ToMaTo/cli/")  # you can use a relative path, or use os.path.expanduser() with a "~"-path
import lib
{% endhighlight %}

{:.alert .alert-info}
This changes the name of the library. In the following, you may need to use `lib` instead of `tomato_lib`

Pro: The library can be updated by fetching the newest updates from the repository.

Con: This solution is not portable, or requires additional set-up when copying your project to a new computer. The ToMaTo library is always called `lib` which may be conflicting with other libraries, and is harder to understand when reading your code.

## The API Proxy

{:.alert .alert-info}
From here on, it is assumed that you can import the ToMaTo library as `tomato_library`. You may need to adapt this in your import statements.

The main object to access ToMaTo is a so-called  _API proxy_. To get an API proxy, you must first create a ToMaTo URL:

{% highlight python %}
import tomato_lib

# instead of hardcoding credentials and server, you should make them configurable.
# you should prompt for a password instead of writing it anywhere.
username="yourusername"
password="yourpassword"
hostname="master.tomato-lab.org"
port=8000
protocol="http+xmlrpc"  # use "https+xmlrpc" for secure connections

url = tomato_lib.createUrl(protocol, hostname, port, username, password)
{% endhighlight %}

Now that you have a URL, you can create the proxy.

{% highlight python %}
api = tomato_lib.getConnection(url)
# note: you do not get an Error message if the login fails. This happens only when calling an API method
{% endhighlight %}

That's it! The `api` variable now holds an object that connects to the ToMaTo API.


### Calling API Methods

You can simply call any API method on the API proxy. For example:

{% highlight python %}
# print a list of topology IDs
topologies = api.topology_list()
for t in topologies:
  print t["id"]
{% endhighlight %}


## Advanced Functions
[TODO]

## Catching Errors
[TODO]

