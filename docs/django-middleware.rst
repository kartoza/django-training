Middleware
==========

Middleware processes incoming requests and outgoing responses.

Installing Middleware
---------------------

```
MIDDLEWARE_CLASSES = (
		'qualified.MiddlewareClassName'
```

Processing
----------

The following can be processed on:

- request
- response
- view
- template_response
- exception


Example
-------

```
class LocaleMiddleware(object):

    def process_request(self, request):

        if 'locale' in request.cookies:
            request.locale = request.cookies.locale
        else:
            request.locale = None

    def process_response(self, request, response):

        if getattr(request, 'locale', False):
            response.cookies['locale'] = request.locale
```