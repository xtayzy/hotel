from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}. {self.name}'


class Room(models.Model):
    number = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f'{self.id}. {self.number}'


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    arrival_date = models.DateField()
    departure_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'{self.id}, {self.room}, {self.arrival_date}-{self.departure_date}'

