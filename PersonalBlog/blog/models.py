from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30)
    content = models.TextField(verbose_name="Content", max_length=300)
    publishDate = models.DateTimeField(verbose_name="Published Date", auto_now_add=True)
    updatedDate = models.DateTimeField(verbose_name="Last Updated", auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)