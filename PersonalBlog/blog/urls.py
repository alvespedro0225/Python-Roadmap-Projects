from django.contrib import admin
from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article-list"),
    path("new", views.ArticleCreateView.as_view(), name="article-create"),
    path("article/<int:pk>", views.ArticleDetailView.as_view(), name="article-detail"),
    path("update/<int:pk>", views.ArticleUpdateView.as_view(), name="article-update"),
    path("delete/<int:pk>", views.ArticleDeleteView.as_view(), name="article-delete"),
    path("admin/", admin.site.urls),
]
