from django.shortcuts import render
from django.http import HttpResponse
#from .models import team, team_detail

# Create your views here.
def aboutus(request):
    return render(request, 'aboutus.html',{})
