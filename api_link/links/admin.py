from django.contrib import admin

from .models import Link, Collection

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = "pk", "title"


@admin.register(Collection)
class LinkAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
