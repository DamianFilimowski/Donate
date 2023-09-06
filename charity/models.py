from django.db import models

from accounts.models import CustomUser


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    CHOICES = [
        (1, 'Fundacja'),
        (2, 'Organizacja Pozarządowa'),
        (3, 'Zbiórka Lokalna'),
    ]

    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=CHOICES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name}({self.get_type_display()})'




class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    Institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=16)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,  null=True)
