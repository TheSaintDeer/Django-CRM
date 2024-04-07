from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):

    users = models.ManyToManyField(User)
    name = models.CharField('Chat name', max_length=100)
    icon = models.ImageField('Chat icon', upload_to='icons/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Message(models.Model):

    text = models.TextField('Message text')
    user = models.ForeignKey(User, related_name='messages_user', on_delete=models.PROTECT)
    channel = models.ForeignKey(Channel, related_name='messages_channel', on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}: {self.text}'