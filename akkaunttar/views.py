from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from akkaunttar.forms import RegistrationForm

def ui(request):
    username = None
    if request.user.is_authenticated:
            username = request.user.username
    args = {'userName':username}
    return render(request, 'akkaunttar/ui.html', args)

def tirkelu(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('akkaunttar:login')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'akkaunttar/tirkelu.html', args)

def profil(request):
    args = {"user":request.user}
    return render(request, "akkaunttar/profil.html", args)
