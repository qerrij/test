from django.db import models
from django import forms


class regisrtation(models.Model):
    STATUS = (
        ('1', 'Ученик'),
        ('2', 'Учитель')
    )
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    # choice_field = models.TextField()
    # choice_field = ModelChoiceField()
    choice_field = models.TextField(choices=STATUS)
    email = models.EmailField()
    password1 = models.TextField()
    password2 = models.TextField()

    def __str__(self):
        template = '{0.username} {0.choice_field} {0.password1} {0.password2} {0.email}'
        return template.format(self)


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
