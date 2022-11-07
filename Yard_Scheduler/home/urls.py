from django.urls import path
from home import views

urlpatterns = [
    # path('about/', views.about),
    # path('problem_statement/', views.problem_statement),
    # path('software_design_document/', views.problem_statement),
    path('index/', views.home)
]