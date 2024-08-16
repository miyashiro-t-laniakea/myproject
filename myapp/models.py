from django.db import models

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class RepairJob(models.Model):
    STATUS_CHOICES = [
        ('pending', '待機中'),
        ('in_progress', '進行中'),
        ('completed', '完了'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.description} - {self.vehicle}"