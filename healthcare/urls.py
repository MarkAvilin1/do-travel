from django.urls import path

from healthcare import views

urlpatterns = [
    # English urls
    path('en/hair/', views.hair, name='hair'),
    path('en/dentist/', views.dentist, name='dentist'),
    path('en/ophthalmology/', views.optic, name='optic'),
    path('en/plastic/', views.plastic, name='plastic'),
    path('en/general_treatment/', views.general, name='general'),
    # Arabic urls
    path('ar/hair/', views.hair_ar, name='hair_ar'),
    path('ar/dentist/', views.dentist_ar, name='dentist_ar'),
    path('ar/ophthalmology/', views.optic_ar, name='optic_ar'),
    path('ar/plastic/', views.plastic_ar, name='plastic_ar'),
    path('ar/general_treatment/', views.general_ar, name='general_ar'),
]
