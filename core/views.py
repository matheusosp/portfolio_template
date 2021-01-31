from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
from django.views.generic import DetailView

from .forms import ContactForm
from .models import Projects


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['projects'] = Projects.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request,'Email sent successfully')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error sent email')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class ListProjectView(DetailView):
    model = Projects
    template_name = 'project.html'

    def get_context_data(self, **kwargs):
        context = super(ListProjectView, self).get_context_data(**kwargs)
        context['project'] = Projects.objects.filter(pk=self.kwargs.get('pk'))
    #    print(context.get('object').)

        return context
