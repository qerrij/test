from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('personal_account', views.personal_account, name='personal_account'),
    path('teacher', views.teacher_personal_area, name='teacher'),
    path('create_module', views.create_module, name='create_module'),
    path('create-course', views.create_course, name='create-course'),
    path('statistic', views.statistic, name='statistic'),
    path('detail/<int:id>', views.detail_page, name='detail_page'),
    path('detail_course/<int:id>', views.detail_course, name='detail_course')
]