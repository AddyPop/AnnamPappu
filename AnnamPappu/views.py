from django.shortcuts import redirect, render, HttpResponse

def home(request):
    return HttpResponse('You are home')