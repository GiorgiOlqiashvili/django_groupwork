from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return self.name