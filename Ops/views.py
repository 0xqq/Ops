# -*- coding: utf-8 -*-
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import redirect, render
from assets.models import *
from users.models import UserProfile
from projs.models import Project


def dashboard(request):
    if request.user.is_superuser:
        assets_count = Assets.objects.all().count()
        project_count = Project.objects.all().count()
        user_count = UserProfile.objects.all().count()
        return render(request, 'dashboard.html', locals())
    else:
        return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')


def login(request):
    if request.session.get('username') and request.session.get('lock'):
        del request.session['lock']
        del request.session['username']
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            request.session['username'] = username
            if remember_me is None:
                request.session.set_expiry(0)
            UserProfile.objects.filter(username=username).update(
                login_status=0
            )
            return HttpResponseRedirect('/users/user_center/', locals())
        else:
            if request.method == "POST":
                return render(request, 'login.html', {"login_error_info": "用户名不错存在，或者密码错误！"}, )
            else:
                return render(request, 'login.html')


def logout(request):
    UserProfile.objects.filter(username=request.user).update(
        login_status=1
    )
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def lock_screen(request):
    if request.method == 'GET':
        user = UserProfile.objects.get(username=request.user)
        UserProfile.objects.filter(username=request.user).update(
            login_status=3
        )
        request.session['lock'] = 'lock'
        request.session['referer_url'] = request.META.get('HTTP_REFERER')
        return render(request, 'lockscreen.html', locals())
    elif request.method == 'POST':
        user = auth.authenticate(username=request.session['username'], password=request.POST.get('pwd'))
        if user:
            del request.session['lock']
            referer_url = request.session.get('referer_url')
            return redirect(referer_url)
        return render(request, 'lockscreen.html', {"login_error_info": "密码错误！请确认输入的密码是否正确！"}, )
