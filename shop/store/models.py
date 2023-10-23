from django.db import models
from django.urls import reverse
from shop.settings import AUTH_USER_MODEL

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=123)
    slug = models.SlugField()
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="article_image", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}({self.stock})"
    
    def get_absolute_url(self):
        return reverse("article_detail", {'slug': self.slug})
    
class Commande(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.article.name} ({self.quantity})"
    
class Panier(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    commandes = models.ManyToManyField(Commande)
    ordered = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username