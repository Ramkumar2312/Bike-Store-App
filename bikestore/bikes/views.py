from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def bike_page(request):
    return HttpResponse('bike details')