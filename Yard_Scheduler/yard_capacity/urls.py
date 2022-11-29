from django.urls import path

from yard_capacity import views

from yard_capacity.views import *

urlpatterns = [
    path('list_tracks_api/', views.list_tracks_api),
    path('upload_file/', views.upload_file),
    path('FileUploadView/', FileUploadView.as_view())
]
