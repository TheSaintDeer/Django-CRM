from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Lead(models.Model):

    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    age = models.IntegerField('Age', default=0)

    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Agent(models.Model):

    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'