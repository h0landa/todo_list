from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=40, null=False)
    description = models.TextField(null=False)
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
