from django.contrib import admin
from .models import Movie, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # NUEVO
    list_display = ('id', 'name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # CAMBIO
    list_display = ('id', 'title', 'release_date')
    filter_horizontal = ('genres',)