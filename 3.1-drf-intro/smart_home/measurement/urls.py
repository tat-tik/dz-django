from django.contrib import admin
from django.urls import path

from measurement.views import SensorView, MeasurementView, AllSensorView, CreateSensorView, UpdateSensorView, CreateMeasurementView, SensorRetrieveView

urlpatterns = [
    path('sensor/', AllSensorView.as_view()),
    path('sensor/create/', CreateSensorView.as_view()),
    path('sensor/update/<pk>/', UpdateSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurements/create/', CreateMeasurementView.as_view()),
    path('sensor/full_list/', SensorView.as_view()),
    path('sensor/<pk>/', SensorRetrieveView.as_view()),
]