from django.conf.urls import url
from django.urls.conf import include, path
from . import views


urlpatterns = [
    path('', views.blog, name="blog"),
]