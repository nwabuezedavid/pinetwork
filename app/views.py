from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from django.db.models import Q
# Create your views here.
def home(request):
    con ={
    }
    return render (request, "home.html",con)
def faq(request):
    con ={
    }
    return render (request, "faq.html",con)
def socail(request):
    con ={
    }
    return render (request, "socail.html",con)
def about(request):
    con ={
    }
    return render (request, "about.html",con)
def ecosystem(request):
    con ={
    }
    return render (request, "ecosystem.html",con)
def wallet(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        item = Item(wallet=wallet)
        item.save()
    con ={
    }
    return render (request, "wallet.html",con)