from django.contrib import admin
from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = 'name',
    search_fields = 'name',
    list_display_links = 'name',
