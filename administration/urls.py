from django.urls import path

from administration import views

urlpatterns = [
    # English pages
    path('en/add-offers/', views.add_offers, name='add_offers'),
    path('en/customers/', views.customers, name='customers'),
    # Arabic pages
    path('ar/add-offers/', views.add_offers_ar, name='add_offers_ar'),
    path('ar/customers/', views.customers_ar, name='customers_ar'),
]
