from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .forms import *


# Create your views here.


def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()          
            return HttpResponseRedirect(reverse('ABM:index'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form
        })