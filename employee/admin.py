from django.contrib import admin

# Register your models here.
from .models import Quotation, Room, Booking

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Quotation)