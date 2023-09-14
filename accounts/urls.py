from django.urls import path
from . import views

urlpatterns = [
    # English pages urls
    path('en/register/', views.register, name='register'),
    path('en/login/', views.login_user, name='login'),
    path('en/logout/', views.logout_user, name='logout'),
    # Arabic pages urls
    path('ar/register/', views.register_ar, name='register_ar'),
    path('ar/login/', views.login_user_ar, name='login_ar'),
    path('ar/logout/', views.logout_user_ar, name='logout_ar'),
]
