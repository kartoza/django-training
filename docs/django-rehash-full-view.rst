Full Views
==========

We are going through all possible views.

View
----

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



