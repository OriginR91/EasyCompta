import sys
from django.shortcuts import render, loader, get_object_or_404
from django.http import HttpResponseRedirect
from Client.forms import ClientForm
from Client.models import Client

# Create your views here.
def homeClient(request) :
    clients = Client.objects.all()
    context = {
        'clients': clients if len(clients) > 0 else 'Pas de clients.',
        'fileCss': sys._getframe().f_code.co_name
    }
    return render(request, 'homeClient.html', context)

def addClient(request) :
    if request.method == 'POST' :
        form = ClientForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/Client/')
    else :
        form = ClientForm()

    context = {
        'form': form,
        'fileCss': sys._getframe().f_code.co_name
    }
    return render(request, 'addClient.html', context)

def detailClient(request, pk=0) :
    if pk > 0 :
        cl = get_object_or_404(Client, pk=pk)
        context = {
            'fileCss': sys._getframe().f_code.co_name,
            'client': cl
        }
        return render(request, 'detailClient.html', context)
    else :
        return HttpResponseRedirect('/Client/')

def manageClient(request) :
    pass