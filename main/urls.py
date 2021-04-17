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
    path('teacher', views.create_module, name='teacher'),
    path('create-course', views.create_course, name='create-course'),
    path('detail/<int:id>', views.detail_page, name='detail_page')
]