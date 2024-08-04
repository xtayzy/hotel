from django.contrib import admin

# Register your models here.

from hotel.models import Type, Room, Reservation

admin.site.register(Type)
admin.site.register(Room)
admin.site.register(Reservation)