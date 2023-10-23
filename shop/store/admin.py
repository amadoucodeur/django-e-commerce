from django.contrib import admin
from store.models import Article, Commande, Panier

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name","stock"]


admin.site.register(Article,ArticleAdmin)
admin.site.register(Commande)
admin.site.register(Panier)

