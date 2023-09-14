from django.urls import path

from tourism import views

urlpatterns = [
    # English urls
    path('en/tickets/', views.tickets, name='tickets'),
    path('en/booking/', views.booking, name='booking'),
    path('en/trips/', views.trips, name='trips'),
    path('en/visas/', views.visas, name='visas'),
    path('en/education/', views.education, name='education'),

    # Arabic urls
    path('ar/tickets/', views.tickets_ar, name='tickets_ar'),
    path('ar/booking/', views.booking_ar, name='booking_ar'),
    path('ar/trips/', views.trips_ar, name='trips_ar'),
    path('ar/visas/', views.visas_ar, name='visas_ar'),
    path('ar/education/', views.education_ar, name='education_ar'),
]
