from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'headline', 'author',
                    'date_published', 'is_draft')
    list_display_links = ('id', 'title')
    list_editable = ('is_draft',)
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Post, PostAdmin)
