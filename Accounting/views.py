import sys
from django.shortcuts import render, loader
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def homeAccounting(request) :
    template = loader.get_template('homeAccounting.html')
    context = {
        'fileCss': sys._getframe().f_code.co_name
    }
    return HttpResponse(template.render(context, request))

def devis(request) :
    return HttpResponse("Devis")

def facture(request) :
    return HttpResponse("Facture")