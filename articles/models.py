from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='articles/')
    author = models.CharField(max_length=100)
    short_description = models.TextField()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Viewpoint(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    email = models.EmailField()
    viewpoint = models.TextField()
    article_page = models.CharField(max_length=100, verbose_name="صفحه مقاله", db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} {self.family}"
