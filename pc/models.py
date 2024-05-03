from django.db import models


# Create your models here.


class Computer(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        db_table = 'Computer'

    def __str__(self):
        return self.model


class GamingComputer(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    video_card = models.CharField(max_length=200)

    class Meta:
        db_table = 'GamingComputer'

    def __str__(self):
        return self.model
