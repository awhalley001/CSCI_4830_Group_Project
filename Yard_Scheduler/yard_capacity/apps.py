# config app to be used throughout project

from django.apps import AppConfig


class YardCapacityConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "yard_capacity"
