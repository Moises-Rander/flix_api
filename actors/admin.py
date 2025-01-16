from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'birthday', 'nationality',
    ordering = 'name',
    search_fields = 'name',
    list_display_links = 'name',
