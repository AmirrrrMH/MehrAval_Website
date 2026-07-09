from django.contrib import admin
from .models import Article, Viewpoint
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Viewpoint)
class ViewpointAdmin(admin.ModelAdmin):
    list_display = ['name', 'family', 'email', 'article_page', 'created_at']
    list_filter = ['article_page', 'created_at']
    search_fields = ['name', 'family', 'email', 'viewpoint', 'article_page']
