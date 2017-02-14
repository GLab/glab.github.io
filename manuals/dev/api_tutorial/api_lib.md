---
layout: manual
title: Testbed Manager Manual
manual: dev
manpage: api_tutorial/api_lib
category: manuals
---

# API Tutorial: Connecting via Library

This tutorial will walk you through the steps of connecting your own Python program to ToMaTo by using the ToMaTo library.

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

The library is available at `~/ToMaTo/cli/lib`. To add it to your project, you can use a symbolic link:

{% highlight bash %}
cd ~/myapp
ln -s ~/ToMaTo/cli/lib tomato_lib
{% endhighlight %}

And in your app:

{% highlight python %}
import tomato_lib
{% endhighlight %}


## creating an API proxy

The main object to access the ToMaTo API is a so-called _API proxy_. To get an API proxy, you must first create a ToMaTo URL:

{% highlight python %}
import tomato_lib
import getpass

# prompt user for credentials
username = raw_input("Username: ")
password = getpass.getpass("Password: ")

hostname = "master.tomato-lab.org"
port = 8000
protocol = "http+xmlrpc"  # use "https+xmlrpc" for secure connections

url = tomato_lib.createUrl(protocol, hostname, port, username, password)
{% endhighlight %}

Now that you have a URL, you can create the proxy.

{% highlight python %}
api = tomato_lib.getConnection(url)
# note: you do not get an Error message if the login fails. This happens only when calling an API method
{% endhighlight %}

That's it! The `api` variable now holds an object that connects to the ToMaTo API.


## Using the API proxy

You can simply call any API method on the API proxy. For example:

{% highlight python %}
# print a list of topology IDs
topologies = api.topology_list()
for t in topologies:
  print t["id"]
{% endhighlight %}

I don't think we have to go further into API usage at this moment. However, there is one thing you should know: The `upload_download` module in the library provides easy methods for uploading or downloading images or executable archives, similar to what is available in the CLI. The difference here is that all these methods require you to hand over the API proxy in order to work:

{% highlight python %}
from tomato_lib import getConnection, createURL
from tomato_lib.upload_download import upload_and_use_rextfv

api = getConnection(createURL(**kwargs))
element_id = "put element ID here"
archive_filename="/path/to/valid/targz.tar.gz"
upload_and_use_rextfv(api, element_id, filename, False)
{% endhighlight %}

## Conclusion

You have now learned how to include the ToMaTo library in your project and use the API proxy to run API calls.

Congratulations! You have finished the API tutorial! For more information, please read the other sections of this manual.

