from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post

# Create your views here.
def  programs(request):
    return render(request, 'programs.html',{})
