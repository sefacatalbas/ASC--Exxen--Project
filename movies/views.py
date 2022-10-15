from django.shortcuts import render
from .models import * #Varan 2
# Create your views here.

def index(request):  #Varan 1
    filmler = Movie.objects.all()
    context = {
        'filmler':filmler
    }
    return render(request, 'exxen.html', context) # context unutma...!!!!
    