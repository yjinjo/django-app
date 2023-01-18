"""mysite url configuration

the `urlpatterns` list routes urls to views. for more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
examples:
function views
    1. add an import:  from my_app import views
    2. add a url to urlpatterns:  path('', views.home, name='home')
class-based views
    1. add an import:  from other_app.views import home
    2. add a url to urlpatterns:  path('', home.as_view(), name='home')
including another urlconf
    1. import the include() function: from django.urls import include, path
    2. add a url to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("account/login/", LoginView.as_view(), name="login"),
    path(
        "account/logout/",
        LogoutView.as_view(),
        name="logout",
        kwargs={"next_page": "/"},
    ),
]
