View
====

This is the parent type that all other views inherit from.

For safety reasons the website has CRFS enabled. Let's disable to test all
our methods.

In the base settings file please comment out:

```
'django.middleware.csrf.CsrfViewMiddleware'
```

Have a look at our class:

```
AllRequestTypes(View):
```

We have written a method for each of the request types.

Try them out online at [all request page](http://0.0.0.0:888/request-types/)

All possible methods are not easy from the browser, so let's use curl


    curl -X GET http://0.0.0.0:888/request-types/

    curl -X POST http://0.0.0.0:888/request-types/

    curl -X PUT http://0.0.0.0:888/request-types/

    curl -X DELETE http://0.0.0.0:888/request-types/

    curl -X PATCH http://0.0.0.0:888/request-types/


Exercise
--------

The full html response is not needed when a curl, or any non-browser request
is made. Add a new template and create a new class to handle this on the
url ```http://0.0.0.0:888/request-types-slim/```


TemplateView
------------

The template view is useful, if we just need to display a template.

have a look at our landing page

```
LandingPage(TemplateView)
```

Exercise
--------

Create a new view to serve up the brochure. Please use:
```http://0.0.0.0:888/brochure/```


RedirectView
------------

These views are used to redirect users to other urls.

have a look at our to view:

```
ToLandingPage(RedirectView)
```

Exercise
--------

There is a url sent out in an email with the link
```http://0.0.0.0:888/h/``` as our landing page. This needs to be redirected.



Detail Views
------------

This is meant to display the details of a model.
The DetailView expects you to specify two things the template to use (as do
all views) and the model. It is important to note that if we wish to use this
method we need to use the private key default variable ``pk``.


Exercise
--------

Create a detail view showing the details of a zone at ``zone/1``. Hint use
``{{ object }}`` in the template


List Views
----------

The ListView lets us show all of our items. Let's set up a list view for our
ZoneTypes. Add the following view::

    class ZoneListView(ListView):
        model = ZoneType
        paginate_by = 5
        template_name = "zones_list.html"


Other options:
- ``context_object_name``: specifies the name to use other than object_list
- ``queryset = ZoneType.objects.all()``:  is an alternative to specifying the model.


Add the url::

    url(r'^list-zones', ZoneListView.as_view())


Add the following html to the template::

     {% if object_list %}
        <table id="zones">
            {% for zone in object_list %}
                <tr>
                    <td>{{ zone.id }}</td>
                    <td>{{ zone.name }}</td>
                </tr>
            {% endfor %}
        </table>
        {% if is_paginated %}
            <div class="pagination">
                <span class="page-links">
                    {% if page_obj.has_previous %}
                        <a href="/list-zones?page={{ page_obj.previous_page_number }}">previous</a>
                    {% endif %}
                    <span class="page-current">
                        Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
                    </span>
                    {% if page_obj.has_next %}
                        <a href="/list-zones?page={{ page_obj.next_page_number }}">next</a>
                    {% endif %}
                </span>
            </div>
        {% endif %}
    {% else %}
        <h3>No Zone Types</h3>
        <p>No cars found!!! :(</p>
    {% endif %}


Form View
---------

The form view gives a default behaviour to django FormClass. If the form is
invalid the form will be displayed again but with validation notes.


CRUD View
---------

The sole purpose of these view is to perform CRUD operations on model objects.
We are currently using the CreateView and the UpdateView in ``AddZoneView`` and
``EditZoneView``.

Exercise
--------

Add the third of these crud views, a DeleteView.


Other Views:

The date based views rely on object creation dates to display these.

 - ArchiveIndexView
 - YearArchiveView
 - MonthArchiveView
 - WeekArchiveView
 - DayArchiveView
 - TodayArchiveView
 - DateDetailView

Mixins
======

Provide a generic way to add functionality to multiple types of views.

Context Mixin
-------------

Often we would like to add some context that is relevant across request types
or we might even not want to overwrite the request functionality. To update the
context without touching the default methods on the class based views, we
can inherit some functionality for the ContextMixin. By adding this to our
landing page, we could add the zones to the page.

Add the parent class ``ContextMixin`` to the landing page.

Now add the method::

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        context['zones'] = InterestZone.objects.all()
        return context


Template Response Mixin
-----------------------

TemplateResponseMixin provides a render_to_response() method, which can be
used to do some template rendering after context is received. A use case for
this mixin is to select a template on the fly.


Single Object Mixin
-------------------

The SingleObjectMixin provides a ``get_object`` method, this allows us to
specify how a object is obtained in form and other views.


Exercise
--------

Add a pk to the brochure url and add the SingleObjectMixin to the Brochure
View. Then display the object details in the Brochure.


Single Object Template Response Mixin
-------------------------------------

The SingleObjectTemplateResponseMixin is a combination of the
SingleObjectMixin and the TemplateResponseMixin.

Multiple Object Template ResponseMixin
--------------------------------------

The MultipleObjectTemplateResponseMixin is a combination of the
Multiple Object Mixin and the Template Response Mixin


Multiple Object Mixin
---------------------

Add a list of objects to a view.

FormMixin and ModelFormMixin
----------------------------

These Mixins add the functionality of handling forms to views by adding
``form_valid`` and ``form_invalid``. The first is for generic forms, the
second for model based forms.


Other Mixins
------------

The following Mixins are more less commonly used:

 - ProcessFormView
 - DeletionMixin
 - YearMixin
 - MonthMixin
 - DayMixin
 - WeekMixin
 - DateMixin
 - BaseDateListView


