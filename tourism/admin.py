from django.contrib import admin

# Register your models here.
from tourism.models import Ticket, Booking, Trip, Visa, Education

admin.site.register(Ticket)
admin.site.register(Booking)
admin.site.register(Trip)
admin.site.register(Visa)
admin.site.register(Education)
