from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm, CreationModule, CreationCourse, FriendForm
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
            # print(user)
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
        # print(Module.objects.filter(name=formCourse.cleaned_data['name']).exclude(author=request.user).order_by('-id')[:1][0])
        a = Module.objects.filter(name=form.cleaned_data['name']).order_by('-id')[:1][0]
        c = a.set_author(user=request.user)
        a.save()
        MC=ModuleCourse(
            course_id=Course.objects.filter(name1=formCourse.cleaned_data['name1']).order_by('-id')[:1][0],
            module_id=Module.objects.filter(name=form.cleaned_data['name']).order_by('-id')[:1][0])
        MC.save()
    form = CreationModule()
    formCourse = CreationCourse()
    return render(request,   'main/teacher-personal.html', {"form": form, "formCourse": formCourse})


def create_course(request):
    if 'add-course' in request.POST:
        formCourse = CreationCourse(request.POST)
        if formCourse.is_valid():
            formCourse.save()
        # print(Course.objects.filter(name1=formCourse.cleaned_data['name1']))
        MC=ModuleCourse(
            course_id=Course.objects.filter(name1=formCourse.cleaned_data['name1']).order_by('-id')[:1][0],
            module_id=Module.objects.filter(author=request.user).order_by('-id')[:1][0])
        MC.save()
    formCourse = CreationCourse()
    return render(request, 'main/create-course.html', {"formCourse": formCourse})


def index(request):
    if 'add-friend' in request.POST:
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
        #     print('save')
        # else:
        #     print(form.errors,'________')
    form = FriendForm()
    if request.user.is_authenticated == True:
        form.initial['user'] = CustomUser.objects.filter(id=request.user.id)[0]

    return render(request, 'main/index.html', {'form': form})


def personal_account(request):
    if request.user.choice_field == '1':
        mod = Module.objects.last()
        s = request.user
        studentModules = StudentModule.objects.raw(
            'SELECT main_studentmodule.id, main_studentmodule.module_id_id  FROM main_studentmodule WHERE main_studentmodule.student_id = %s', [s.id]
        )
        course = {}
        for i in studentModules:
            print(i.module_id_id)
            objectModule = Module.objects.raw('SELECT main_module.id FROM main_module WHERE main_module.id = %s',[i.module_id_id])
            # for b in objectModule:
            modul = objectModule[0]
            print(modul)
            cours = Course.objects.raw(
                'SELECT main_course.name1, main_course.id FROM main_course JOIN (SELECT main_modulecourse.course_id_id FROM   main_module  JOIN main_modulecourse  ON %s = main_module.id and main_modulecourse.module_id_id = %s) MC ON MC.course_id_id = main_course.id',
                [i.module_id_id, i.module_id_id])
            coursObj =[]
            for b in cours:
                coursObj.append(b)
                print(b)
            course.update({modul: coursObj})
        return render(request, 'main/student-personal.html', {'course':course})

    else:
        return redirect('teacher')


def detail_page(request, id):
    get_article = Module.objects.get(id=id)
    get_article.status = 1
    print(get_article.status)
    courses = Course.objects.raw(
                'SELECT main_course.name1, main_course.id FROM main_course JOIN (SELECT main_modulecourse.course_id_id FROM   main_module  JOIN main_modulecourse  ON %s = main_module.id and main_modulecourse.module_id_id = %s) MC ON MC.course_id_id = main_course.id',
                [get_article.id, get_article.id])
    request_past = request.META.get('HTTP_REFERER')
    context = {
        'get_article': get_article,
        'courses': courses,
        'request_past': request_past
    }
    template = 'main/detail.html'
    return render(request, template,  context)


def detail_course(request, id):
    get_course = Course.objects.get(id=id)
    context = {
        'get_course': get_course,
    }
    template = 'main/detail_course.html'
    return render(request, template,  context)


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
