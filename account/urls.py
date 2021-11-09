from django.urls.conf import include, path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),    
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),   
    path('admin/', views.admin, name="admin"),
    path('customer/', views.customer, name="customer"),
    path('employee/', views.employee, name="employee"),
]