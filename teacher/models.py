from django.db import models
class Teacher(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    country=models.CharField(max_length=20)
    total_amount_paid=models.PositiveSmallIntegerField()
    experience=models.PositiveSmallIntegerField()
    age=models.PositiveSmallIntegerField()
    level_of_education=models.CharField(max_length=15)
    unit_taught=models.CharField(max_length=10)


