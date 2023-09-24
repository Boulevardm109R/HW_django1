from django.urls import path
from first_take import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('current_time/', views.current_time_view, name='current_time'),
    path('workdir/', views.workdir_view, name='workdir'),
]
