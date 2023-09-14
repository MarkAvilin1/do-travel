from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts import views
from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # English
    path('', views.home, name='home'),
    path('en/offer_details/<int:pk>/', views.offer_details, name='offer_details'),
    path('en/delete_offer/<int:pk>/', views.delete_offer, name='delete_offer'),
    path('en/about/', views.about, name='about'),
    path('en/contacts/', views.contacts, name='contacts'),
    # Ararbic
    path('ar/home/', views.home_ar, name='home_ar'),
    path('ar/offer_details/<int:pk>/', views.offer_details_ar, name='offer_details_ar'),
    path('ar/delete_offer/<int:pk>/', views.delete_offer_ar, name='delete_offer_ar'),
    path('ar/about/', views.about_ar, name='about_ar'),
    path('ar/contacts/', views.contacts_ar, name='contacts_ar'),
    # others
    path('auth/', include('accounts.urls')),
    path('tour/', include('tourism.urls')),
    path('health/', include('healthcare.urls')),
    path('site_admin/', include('administration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
