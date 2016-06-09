Templates
=========

So far we have been using variables in templates and some template tags.
These are identifiable by the ``{{`` and ``{%`` respectively.

Template variables are handed to the renderer as context.

Template Hierarchy
------------------

With the goal of minimizing repetition templates can extend each other or be
included into each other. This can be thought of as subclassing of the templates.

We will be using base.html as our base template.

Specifically take note of the blocks::

    {% block navigation %}{% endblock %}
    {% block contents %}{% endblock %}

All blocks can be replaced in any template that extends this templates.

Since our views only know which template they would like to load, each
template should specify the template that it is based off. This is done by
adding the following at the top of the file::

	{% extends "base.html" %}

including another template in our current template is done as follows::

	{% block navigation  %}
		{% include "navigation.html" %}
	{% endblock %}

Exercise
--------

Update our landing page template to extend the base.html file. Create a new
navigation.html file.

The navigation file could look something like::

    <ul>
        <li><a href="/">Home</a></li>
        ...
    </ul>
