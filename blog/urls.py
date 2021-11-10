from django.conf.urls import url
from django.urls.conf import  path
from . import views


urlpatterns = [
    path('', views.blog, name="blog"),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:pk>/', views.EditBlog.as_view(), name='edit_blog'),
]