from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models


class SchoolListView(ListView):
    # You will be provided with a list of every record
    model = models.School


class SchoolDetailView(DetailView):
    model = models.School
    template_name = "basic_app/school_detail.html"
