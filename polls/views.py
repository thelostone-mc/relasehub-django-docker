from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Random Index Route.")


def derp(request):
    return HttpResponse("Another Derp Derp")
