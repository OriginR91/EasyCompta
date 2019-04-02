from django.shortcuts import render, loader

# Create your views here.
def home(request) :
    context = {}
    return render(request, 'homeClient.html', context)