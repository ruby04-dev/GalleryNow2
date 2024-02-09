
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

# Register your models here.
admin.site.register(User, UserAdmin)
