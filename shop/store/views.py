from django.shortcuts import render, get_object_or_404, redirect
from store.models import Article, Panier, Commande
from django.urls import reverse

# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request,'store/home.html', context={"articles":articles})

def article_detail(request, slug):
    article_detail = get_object_or_404(Article, slug=slug)
    return render(request, 'store/detail.html', context={'article_detail': article_detail})

def ajout_au_panier(request, slug):
    user = request.User
    get_object_or_404(Article, slug=slug)
    panier , _ = Panier.objects.get_or_create(user=user)
    commande, commande_created = Commande.objects.get_or_create(user=user,article_detail=article_detail)

    if commande_created:
        panier.commandes.add(commande)
        panier.save()
    else:
        commande.quantity += 1
        commande.save()

    return redirect(reverse("article_detail"))
