from django.contrib import admin
from .models import MenuItem
# Register your models here.
from .models import Reservation
admin.site.register(Reservation)
admin.site.register(MenuItem)