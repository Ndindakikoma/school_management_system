from django.http import HttpResponse
from django.shortcuts import render


def demoPage(request):
    return render(request, 'school_management/demo.html')
