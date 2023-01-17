from django.shortcuts import render
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from . import models
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class SchoolListView(ListView):
    context_object_name = "schools"
    # You will be provided with a list of every record
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    # Once you've successfully deleted a school, I want you to
    # go back to the list page of the basic app and show all the schools.
    # The reason why I use `reverse_lazy` is I want it to wait until
    # it's actually called as a success.
    success_url = reverse_lazy("basic_app:list")
