from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)
    release_year = models.PositiveSmallIntegerField(null=True, blank=True)
    category = models.CharField(max_length=120, blank=True)
    rating = models.CharField(max_length=20, blank=True)
    poster_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-is_featured", "-release_year", "title"]

    def __str__(self):
        return self.title
