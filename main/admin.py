from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


# def add_rote():



class No_rote(admin.ModelAdmin):
    actions = []


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'choice_field', 'email', 'password1', 'password2']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Module)
admin.site.register(Friend)
admin.site.register(Course)
admin.site.register(Cases)
admin.site.register(Project)
admin.site.register(CourseCase)
admin.site.register(ModuleCourse)
admin.site.register(StudentModule)
admin.site.register(StudentProject)