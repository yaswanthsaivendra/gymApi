from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Gym(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} owned by {self.user}"


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    gym = models.OneToOneField(Gym, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class WorkoutSession(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return f"{self.client.name} - {self.date}"


