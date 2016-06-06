__author__ = 'Christian Christelis <christian@kartoza.com>'
__date__ = '05/06/16'

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin

from demo_app.models import InterestZone
from demo_app.forms import InterestZoneForm


class LandingPage(TemplateView, ContextMixin):
    template_name = "landing_page.html"

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        context['zones'] = InterestZone.objects.all()
        return context

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
