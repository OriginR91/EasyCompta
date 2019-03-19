from django.shortcuts import render, loader
from django.http import HttpResponse, HttpResponseRedirect
from User.forms import UserForm
import sys

# Globals
fileCss = ""

def index(request) :
    template = loader.get_template('User/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def subscribe(request) :
    fileCss = sys._getframe().f_code.co_name

    if request.method == 'POST' :
        form = UserForm(request.POST)
        if form.is_valid() :
            if(request.POST.get('password') == request.POST.get('passwordVerif')) :
                form.save()
                return HttpResponseRedirect('/User/')
            else :
                return HttpResponseRedirect('/User/subscribe/error')
    else :
        form = UserForm()
        template = loader.get_template('User/subscribe.html')
        context = {
            'form': form,
            'fileCss': fileCss
        }
        return HttpResponse(template.render(context, request))

def getUser(request, user) :
    template = loader.get_template('User/user.html')
    context = {}
    return HttpResponse(template.render(context, request))
