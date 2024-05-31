from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


    class Meta:
        ordering = ['id']
        db_table='sensor'
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"
    def __str__(self):
        return f'{self.name}'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=6, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sensor']
        db_table = 'measurement'
        verbose_name = "Измерение"
        verbose_name_plural = "Измерения"

    def __str__(self):
        return f'{self.sensor.name} : {self.created_at}'
