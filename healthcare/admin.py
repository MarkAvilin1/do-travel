from django.contrib import admin

from healthcare.models import Dentist, Hair, Plastic, General

admin.site.register(Dentist)
admin.site.register(Hair)
admin.site.register(Plastic)
admin.site.register(General)
