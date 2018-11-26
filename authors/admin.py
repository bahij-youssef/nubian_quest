from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'creation_date')
    list_display_links = ('id', 'first_name', 'last_name')


admin.site.register(Author, AuthorAdmin)
