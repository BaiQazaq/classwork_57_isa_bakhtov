from django.contrib import admin

from webapp.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at")
    list_filter = ("id", "title", "author", "created_at")
    search_fields = ("title", "author")
    fields = ("title", "author", "text", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Article, ArticleAdmin)