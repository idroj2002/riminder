from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Reminder(models.Model):
    title = models.CharField(max_length=200, default="Reminder")
    description = models.TextField()
    reminder_date = models.DateTimeField()

    def __str__(self):
        return f"Recordatori per {self.title} el {self.reminder_date}"
