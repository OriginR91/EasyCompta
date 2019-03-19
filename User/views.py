from django.shortcuts import render, loader
from django.http import HttpResponse, HttpResponseRedirect
from User.forms import UserForm

def index(request) :
    template = loader.get_template('User/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def subscribe(request) :
    if request.method == 'POST' :
        return HttpResponseRedirect('/User/')
    else :
        form = UserForm()
        template = loader.get_template('User/subscribe.html')
        context = {
            'form': form
        }
        return HttpResponse(template.render(context, request))

def getUser(request, user="ok") :
    user = "none"
    template = loader.get_template('User/user.html')
    context = {}
    return HttpResponse(template.render(context, request))