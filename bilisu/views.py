from django.shortcuts import render, redirect

# Create your views here.
def login_redirect(request):
    return redirect('akkaunttar/login')
