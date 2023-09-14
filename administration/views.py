from django.contrib.auth import admin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required


from healthcare.models import *
from tourism.models import *
from .models import OffersEN, OfferAr


# English Pages
@permission_required('auth.admin')
def add_offers(request):
    success = ''
    if request.method == 'POST':
        title = request.POST.get('title', 'NO')
        description = request.POST.get('description', 'NO')
        image = request.FILES['image']
        OffersEN(title=title, description=description, image=image).save()
        success = "You have upload new offer successfully!"
        return redirect('home')
    context = {'msg': success}
    return render(request, 'en/admin/add_offers.html', context)


@permission_required('auth.admin')
def customers(request):
    context = {
        'tickets': Ticket.objects.all(),
        'booking': Booking.objects.all(),
        'trips': Trip.objects.all(),
        'visas': Visa.objects.all(),
        'education': Education.objects.all(),
        'hair': Hair.objects.all(),
        'optic': Optic.objects.all(),
        'dentist': Dentist.objects.all(),
        'plastic': Plastic.objects.all(),
        'general': General.objects.all(),
    }
    return render(request, 'en/admin/customers.html', context)


# Arabic Pages
@permission_required('auth.admin')
def add_offers_ar(request):
    success = ''
    if request.method == 'POST':
        title = request.POST.get('title', 'NO')
        description = request.POST.get('description', 'NO')
        image = request.FILES['image']
        OfferAr(title=title, description=description, image=image).save()
        success = "لقد تم تحميل العرض الجديد بنجاح"
        return redirect('home_ar')
    context = {'msg': success}
    return render(request, 'ar/admin/add_offers.html', context)


@permission_required('auth.admin')
def customers_ar(request):
    context = {
        'tickets': Ticket.objects.all(),
        'booking': Booking.objects.all(),
        'trips': Trip.objects.all(),
        'visas': Visa.objects.all(),
        'education': Education.objects.all(),
        'hair': Hair.objects.all(),
        'optic': Optic.objects.all(),
        'dentist': Dentist.objects.all(),
        'plastic': Plastic.objects.all(),
        'general': General.objects.all(),
    }
    return render(request, 'ar/admin/customers.html', context)
