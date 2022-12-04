from typing import ItemsView
from django.contrib import admin
from .models import Yard, Car, Testyard
# Register your models here.
admin.site.register(Yard)
admin.site.register(Car)
admin.site.register(Testyard)