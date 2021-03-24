from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {str(self.done)}'