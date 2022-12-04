from django.urls import path

from yard_capacity import views

from yard_capacity.views import *
# all urls for yard capcity application
urlpatterns = [
    path('list_tracks_api/', views.list_tracks_api),
    path('FileUploadView/', FileUploadView.as_view()),
    path('yard_tracks/', views.yard_tracks),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("yard/", views.yard, name="yard"),
    path("create/", views.create, name="create"),
]

