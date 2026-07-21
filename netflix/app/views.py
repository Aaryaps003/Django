from django.shortcuts import render
from .models import Movie
# Create your views here.
def home(request):


    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies':movies})