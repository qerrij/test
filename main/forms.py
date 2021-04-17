from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


STATUS = (
        ('1', 'Ученик'),
        ('2', 'Учитель')
)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'choice_field', 'email', 'password1', 'password2']


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'choice_field', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'choice_field': forms.RadioSelect,
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['choice_field'].empty_label = 'Please Select'


class CreationModule(ModelForm):
    DONE = {
        ('0', 'START'),
        ('1', 'CONTINUE'),
        ('2', 'STOP')
    }
    name = forms.CharField(label='Название модуля', widget=forms.TextInput(attrs={'class': 'name'}))
    status = forms.ChoiceField(widget=forms.Select, choices=DONE)
    class Meta:
        model = Module
        fields = ['name', 'status']


class FriendForm(ModelForm):
    # users = [i.username for i in CustomUser.objects.raw('SELECT id FROM main_customuser')]
    # print(users)
    # user = forms.ChoiceField()
    # friend = forms.ChoiceField(widget=forms.Select, choices=users)
    # friend = forms.ChoiceField(widget=forms.Select, choices=users)
    class Meta:
        users = [i.username for i in CustomUser.objects.raw('SELECT id FROM main_customuser')]
        print(users)
        model = Friend
        fields = ['user', 'friend']
        widgets = {
            'user': forms.HiddenInput(),
            'friend': forms.Select(choices=users)
        }

class CreationCourse(ModelForm):
    name1 = forms.CharField(label='Название курса', widget=forms.TextInput(attrs={'class': 'name1'}))
    information = forms.CharField(label='Ссылка на видеоурок', widget=forms.TextInput(attrs={'class': 'inf'}))

    class Meta:
        model = Course
        fields = ['name1', 'information']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
