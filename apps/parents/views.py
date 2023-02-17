from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Parent


class ParentListView(ListView):
    model = Parent


class ParentDetailView(DetailView):
    model = Parent
    template_name = "parents/parent_detail.html"


class ParentCreateView(SuccessMessageMixin, CreateView):
    model = Parent
    fields = "__all__"
    success_message = "New staff successfully added"

    def get_form(self):
        """add date picker in forms"""
        form = super(ParentCreateView, self).get_form() 
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 1})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 1})
        return form


class ParentUpdateView(SuccessMessageMixin, UpdateView):
    model = Parent
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(ParentUpdateView, self).get_form()
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 1})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 1})
        return form


class ParentDeleteView(DeleteView):
    model = Parent
    success_url = reverse_lazy("parent-list")