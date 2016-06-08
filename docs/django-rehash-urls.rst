Urls
====

The urls file defines all possible paths that our application will deal with.
Anything that falls outside of this is served a 404.

Regular Expressions
-------------------

Simple cases can be handled by static urls, but this is usually not enough.
In most cases we would like to decode some bit of information from the
url that is being requested. Let's say we want to give the users a
specific year's interest zones, we could do this::

    url(r'^zone/2016/$, view_for_this_year)

but then next year we would have to update that to ::

    url(r'^zone/2016/$, view_for_last_year)
    url(r'^zone/2017/$, view_for_this_year)

we could use a regular expression in this way:

    url(r'^zone/(20[0-1][0-9])/$, view_for_any_year)

Let's look at the elements we used there:

- ``^...`` start of regular expression.
- ``...$`` terminate matching. (Leave this out if we add a new set of urls.
- ``r'...`` tells python to handle this as a raw string.
- ``( ... )`` specifies what we would like to capture
- ``[ ... ]`` specifies the expected range of values expected here

Other options include:

- ``\d`` match a didgit
- ``\w`` match a character

Following a capture area we can specify the number of occurrences of this type

- ``+`` one or more
- ``*`` zero or more
- ``{n} where n is the precise number of occurances

Named groups can reference it as such in our view.

- ``(?P<name>pattern)`` gives the variables we are expecting a specific name.

