from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = 'rate',
    list_display = 'title', 'release_date',
    ordering = 'title',
    list_filter = 'title', 'genres'
    search_fields = 'title', 'genres__name', 'actors__name', 'resume',
    list_display_links = 'title',
