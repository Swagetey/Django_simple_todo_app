from home.models import Contact
from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("Hello Django App")

