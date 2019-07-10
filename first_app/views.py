from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html', {})



def atag_practice(request):
    return render(request, 'first_app/atag_practice.html', {})
