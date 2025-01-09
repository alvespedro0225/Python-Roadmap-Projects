from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from . import owner
from .models import Article

# Create your views here.]


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(owner.OwnerCreateView):
    model = Article
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:article-list")


class ArticleUpdateView(owner.OwnerUpdateView):
    model = Article
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:article-list")


class ArticleDeleteView(owner.OwnerDeleteView):
    model = Article
    success_url = reverse_lazy("blog:article-list")
