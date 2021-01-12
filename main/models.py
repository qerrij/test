from django.db import models
from django import forms


class regisrtation(models.Model):
    STATUS = [
        ('1', 'Ученик'),
        ('2', 'Учитель')
    ]
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    # choice_field = models.TextField()
    # choice_field = ModelChoiceField()
    choice_field = models.TextChoices("1","2")
    email = models.EmailField()
    password1 = models.TextField()
    password2 = models.TextField()

    def __str__(self):
        return self.username, self.choice_field, self.password1, self.password2, self.email


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
