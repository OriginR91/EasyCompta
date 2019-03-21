import sys
from django.shortcuts import render, loader
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from User.forms import UserForm

# Globals
fileCss = ""

def index(request) :
    template = loader.get_template('User/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signin(request) :
    if request.method == 'POST' :
        pass
    else :
        template = loader.get_template('User/signin.html')
        context = {}
        return HttpResponse(template.render(context, request))

def subscribe(request) :
    fileCss = sys._getframe().f_code.co_name

    if request.method == 'POST' :
        form = UserForm(request.POST)
        if form.is_valid() :
            form.save(commit=False)
            if (
                request.POST.get('password') == request.POST.get('passwordVerif') and 
                request.POST.get('email') == request.POST.get('emailConfirm')
            ) :
                form.save()
                return HttpResponseRedirect('/User/')
            else :
                return HttpResponseRedirect('/User/subscribe/error/')
    else :
        form = UserForm()
        template = loader.get_template('User/subscribe.html')
        context = {
            'form': form,
            'fileCss': fileCss
        }
        return HttpResponse(template.render(context, request))

@login_required
def account(request) :
    template = loader.get_template('User/account.html')
    context = {}
    return HttpResponse(template.render(context, request))
