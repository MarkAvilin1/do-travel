from django import forms

from .models import Ticket, Booking, Trip, Visa


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('fullname', 'email', 'phone')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('fullname', 'email', 'phone')


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('fullname', 'email', 'phone')


class VisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ('fullname', 'email', 'phone')
