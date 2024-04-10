from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Channel, Message

# Register your models here.
class ChannelAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'icon')
    search_fields = ('name', 'users')
    list_filter = ('name', 'users')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Message)