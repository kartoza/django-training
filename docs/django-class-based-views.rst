Class Based Views
=================

Traditionally views in django are functions taking requests and returning some 
response. This functional approach precludes many benefits of object
orientation, the most notable being code reuse and inheritance.

The full reference of the built in API can be found at
`class based views <https://docs.djangoproject.com/en/1.9/ref/class-based-views/>`_

Views
-----

Provides specialised setup for specific tasks.

- Simple generic view
 - View
 - TemplateView
 - RedirectView
- Detail Views
 - DetailView
- List Views
 - ListView
- Editing views
 - FormView
 - CreateView
 - UpdateView
 - DeleteView
- Date-based views
 - ArchiveIndexView
 - YearArchiveView
 - MonthArchiveView
 - WeekArchiveView
 - DayArchiveView
 - TodayArchiveView
 - DateDetailView


Mixins
------

Provide a generic way to add functionality to multiple types of views.


- Simple mixins
 - ContextMixin
 - TemplateResponseMixin
- Single object mixins
 - SingleObjectMixin
 - SingleObjectTemplateResponseMixin
- Multiple object mixins
 - MultipleObjectMixin
 - MultipleObjectTemplateResponseMixin
- Editing mixins
 - FormMixin
 - ModelFormMixin
 - ProcessFormView
 - DeletionMixin
- Date-based mixins
 - YearMixin
 - MonthMixin
 - DayMixin
 - WeekMixin
 - DateMixin
 - BaseDateListView


