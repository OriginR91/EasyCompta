import sys
from django.shortcuts import render, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from User.forms import UserForm, ProfilForm

# Globals
fileCss = ""

def index(request) :
    template = loader.get_template('User/index.html')
    context = {
        'test': 'OK'
    }
    return HttpResponse(template.render(context, request))

def user_login(request) :
    if request.method == 'POST' :
        form = UserForm(request.POST)
        if form.is_valid() :
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user :
                login(request, user)
                return HttpResponseRedirect('/User/')
    else :
        form = UserForm()
        context = {
            'form': form,
            'test': 'OK'
        }
        return render(request, 'registration/login.html', context)

def subscribe(request) :
    fileCss = sys._getframe().f_code.co_name

    if request.method == 'POST' :
        formUser = UserForm(request.POST)
        formProfil = ProfilForm(request.POST)
        if formUser.is_valid() and formProfil.is_valid() :
            if (
                request.POST.get('password') == request.POST.get('passwordConfirm') and 
                request.POST.get('email') == request.POST.get('emailConfirm')
            ) :
                user = formUser.save()
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
            'fileCss': fileCss
        }
        return HttpResponse(template.render(context, request))

@login_required
def member(request) :
    template = loader.get_template('User/account.html')
    context = {}
    return HttpResponse(template.render(context, request))