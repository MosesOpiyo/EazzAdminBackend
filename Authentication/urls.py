from django.urls import path
from Authentication import views as views
from rest_framework.authtoken import views as special_views

urlpatterns = [
    path("Registration",views.registration_view,name="registration"),
    path("Login",special_views.obtain_auth_token),
    path("Profile",views.get_profile,name='profile')
]