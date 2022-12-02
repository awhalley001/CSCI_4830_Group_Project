from typing import ItemsView
from django.contrib import admin
from .models import Yard, Item, ToDoList
# Register your models here.
admin.site.register(Yard)
admin.site.register(ToDoList)
admin.site.register(Item)