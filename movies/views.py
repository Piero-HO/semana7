from rest_framework import viewsets
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    # NUEVO
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer