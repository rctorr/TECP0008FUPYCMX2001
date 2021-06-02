from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('zonas/', views.zonas, name="zonas"),
    path("accounts/login/",
        auth_views.LoginView.as_view(template_name="tours/login.html"),
        name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="/"),
        name="logout"),
    path('accounts/profile/', views.tours_profile, name="profile"),
]
