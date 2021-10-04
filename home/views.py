from django.shortcuts import render
#from .models import
#from .models import team_single

#from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html', {})