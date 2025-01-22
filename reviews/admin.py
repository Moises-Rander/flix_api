from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = 'movie__title', 'stars',
    ordering = 'stars',
    list_filter = 'movie__title', 'stars',
    search_fields = 'movie__title', 'comments',
    list_display_links = 'movie__title',
