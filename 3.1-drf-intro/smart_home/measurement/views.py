# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer, \
    MeasurementDetailSerializer



class AllSensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementView(ListAPIView):
        queryset = Measurement.objects.all()
        serializer_class = MeasurementSerializer

class CreateSensorView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class UpdateSensorView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer

class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
class SensorRetrieveView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer