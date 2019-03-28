import sys
from django.shortcuts import render, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from User.forms import UserForm, ProfilForm
from .models import Profil


def index(request) :
    template = loader.get_template('User/index.html')
    context = {
        'test': 'OK'
    }
    return HttpResponse(template.render(context, request))

def subscribe(request) :
    if request.method == 'POST' :
        formUser = UserForm(request.POST)
        formProfil = ProfilForm(request.POST)
        if formUser.is_valid() and formProfil.is_valid() :
            if (
                request.POST.get('password') == request.POST.get('passwordConfirm') and 
                request.POST.get('email') == request.POST.get('emailConfirm')
            ) :
                user = formUser.save(commit=False)
                user.set_password(user.password)
                user.save()

                profil = formProfil.save(commit=False)

                profil.user = user

                formProfil.save()
                return HttpResponseRedirect('/User/')
            else :
                return HttpResponseRedirect('/User/subscribe/error/')
        else :
            return HttpResponseRedirect('/User/')
    else :
        formUser = UserForm()
        formProfil = ProfilForm()
        template = loader.get_template('User/subscribe.html')
        context = {
            'formUser': formUser,
            'formProfil': formProfil,
            'fileCss': sys._getframe().f_code.co_name
        }
        return HttpResponse(template.render(context, request))

@login_required
def member(request) :
    profil = Profil.objects.get(user=request.user)
    template = loader.get_template('User/member.html')
    context = {
        'fileCss': sys._getframe().f_code.co_name,
        'profil': profil
    }
    return HttpResponse(template.render(context, request))

def user_login(request) :
    if request.user.is_authenticated() :
        return HttpResponseRedirect('/User/member/')