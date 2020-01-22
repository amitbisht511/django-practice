# .html"rom django.shortcuts import render
from django.views.generic import ListView

from .models import Movie


# Create your views here.
class MoviesListView(ListView):
    context_object_name = "movies"
    model = Movie
    template_name = "movies/movies_list.html"
