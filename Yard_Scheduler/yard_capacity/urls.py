from django.urls import path

from yard_capacity import views

urlpatterns = [
    path('list_tracks_api/', views.list_tracks_api),
]
