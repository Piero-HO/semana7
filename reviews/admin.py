from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # NUEVO
    list_display = (
        'id',
        'movie',
        'author_name',
        'rating'
    )