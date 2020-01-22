from django.urls import path

from .views import MoviesListView

app_label = "movies"
urlpatterns = [path("", MoviesListView.as_view(), name="movies")]
