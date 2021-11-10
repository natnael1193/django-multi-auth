from django.urls.conf import include, path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login_view/', views.login_view, name="login_view"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name="home"),
    path('admin/', views.admin, name="admin"),
    path('customer/', views.customer, name="customer"),
    path('employee/', views.employee, name="employee"),
    path('not_authenticated/', views.not_authenticated, name="not_authenticated"),
]
