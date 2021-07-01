from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('locations/<str:city>/', views.WeatherView.as_view(), name='weather'),
]