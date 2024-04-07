from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Channel, Message

# Register your models here.
# admin.site.register(User, UserAdmin)
admin.site.register(Channel)
admin.site.register(Message)