from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]


class Article(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]
# Create your models here.
