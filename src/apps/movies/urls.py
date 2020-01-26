from django.urls import path

from .views import MoviesListView

app_name = "movie"
urlpatterns = [path("", MoviesListView.as_view(), name="list")]
