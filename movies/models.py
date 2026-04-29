from django.db import models


class Genre(models.Model):
    # NUEVO
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'genres'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()

    # CAMBIO
    genres = models.ManyToManyField(
        Genre,
        related_name='movies',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'movies'

    def __str__(self):
        return self.title