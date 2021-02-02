from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'choice_field', 'email', 'password1', 'password2']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Cases)
admin.site.register(Project)
# admin.site.register(try_to_die)
