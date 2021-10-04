from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post

# Create your views here.
def partners(request):
    return render(request, 'partners.html',{})
