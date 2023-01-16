from django.urls import path
from . import views

# Template Tagging
app_name = "basic_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("other/", views.other, name="other"),
    path("relative/", views.relative, name="relative"),
]
