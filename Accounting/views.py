from django.shortcuts import render, loader
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request) :
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def devis(request) :
    return HttpResponse("Devis")

def facture(request) :
    return HttpResponse("Facture")