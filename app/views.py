from django.shortcuts import render
from django.http import HttpResponse
import os
from datetime import datetime

def home_view(request):
    return HttpResponse("Home page")

def current_time_view(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current time: {current_time}")

def workdir_view(request):
    workdir_contents = os.listdir()
    return HttpResponse(f"Directory content: {', '.join(workdir_contents)}")