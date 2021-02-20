from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm, CreationModule, CreationCourse
from django.contrib import messages
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib.auth import login, logout


def register(request):
    if 'add' in request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.has_changed():
            print(form.fields['choice_field'])
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
            # print(form.errors.as_data())
            # print(form.cleaned_data)
    form = CustomUserCreationForm()
    return render(request, 'main/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            # if user.choice_field == '1':
            #    return redirect('personal_account')
            # else:
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def create_module(request):
    if 'add' in request.POST:
        form = CreationModule(request.POST)
        formCourse = CreationCourse(request.POST)
        if form.is_valid():
            form.save()
        if formCourse.is_valid():
            formCourse.save()
        MC=ModuleCourse(
            course_id=Course(name=formCourse.name1),
            module_id =Module(name=form.name))
        MC.save()


    form = CreationModule()
    formCourse = CreationCourse()

    return render(request, 'main/teacher-personal.html', {"form": form, "formCourse": formCourse})


# def create_course(request):
#     if 'add-course' in request.POST:
#         formCourse = CreationCourse(request.POST)
#         if formCourse.is_valid():
#             formCourse.save()
#     formCourse = CreationCourse()
#     return render(request, 'main/teacher-personal.html', {"form": formCourse})


# def form(request):
#     if request.method == 'POST':
#         formCourse = CreationModule(request.POST)
#         print(form)
#         if formCourse.is_valid():
#             formCourse.save()
#     formCourse = CreationModule()
#     return render(request, 'main/form.html', {"form": formCourse})


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def personal_account(request):
    # print(request.user)
    if request.user.choice_field == '1':
        # module = Module.objects.all()
        # name_course = Course.objects.all
        # context = {
        #     'module': module,
        #     'name_course': name_course,
        # }
        return render(request, 'main/student-personal.html')

    else:
        return redirect('teacher')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')
        else:
            error = 'Форма была некорректной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
