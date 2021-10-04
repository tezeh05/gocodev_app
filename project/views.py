from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post

# Create your views here.
def project(request):
    return render(request, 'project.html',{})