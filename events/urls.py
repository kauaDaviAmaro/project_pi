from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event_list'),
    path('create/', views.create_event, name='create_event'),
]
