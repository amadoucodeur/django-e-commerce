from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','price','category','date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
