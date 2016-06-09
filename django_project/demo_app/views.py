__author__ = 'Christian Christelis <christian@kartoza.com>'
__date__ = '05/06/16'

from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic import TemplateView, View, RedirectView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.shortcuts import render_to_response

from demo_app.models import InterestZone, ZoneType
from demo_app.forms import InterestZoneForm


class AllRequestTypes(View):
    template_name = "request_types.html"

    def get(self, request):
        context = {
            'request_type': 'GET',
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
            'request_type': 'POST'
        }
        return render(request, self.template_name, context)

    def put(self, request):
        context = {
            'request_type': 'PUT'
        }
        return render(request, self.template_name, context)

    def patch(self, request):
        context = {
            'request_type': 'PATCH'
        }
        return render(request, self.template_name, context)

    def delete(self, request):
        context = {
            'request_type': 'DELETE'
        }
        return render(request, self.template_name, context)


class LandingPage(TemplateView):
    template_name = "landing_page.html"


class ToLandingPage(RedirectView):
    def get_redirect_url(self):
        return reverse('demo_app:index')


class EditZoneView(UpdateView):
    template_name = "zone_form.html"
    form_class = InterestZoneForm
    # success_url = '/'
    model = InterestZone


class AddZoneView(CreateView):
    template_name = "zone_form.html"
    success_url = '/'
    form_class = InterestZoneForm
    model = InterestZone
