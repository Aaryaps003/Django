from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "release_year", "rating", "is_featured")
    list_filter = ("category", "rating", "is_featured")
    search_fields = ("title", "synopsis")
