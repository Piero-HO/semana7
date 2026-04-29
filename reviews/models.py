from django.db import models
from movies.models import Movie


class Review(models.Model):
    # NUEVO
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    author_name = models.CharField(max_length=100)

    rating = models.PositiveSmallIntegerField()

    spoiler_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'reviews'

    def __str__(self):
        return f'{self.author_name} - {self.movie.title}'