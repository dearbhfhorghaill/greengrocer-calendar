from django.urls import path

from . import views

app_name = 'greengrocer_calendar_app'
urlpatterns = [
    path('', views.index, name='index'),
]
