from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'join_date', 'subscribed')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 25


admin.site.register(Subscriber, SubscriberAdmin)
