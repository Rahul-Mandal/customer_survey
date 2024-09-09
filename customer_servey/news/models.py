from django.db import models

# Create your models here.
class Articles(models.Model):
    articles = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    urlToImage = models.CharField(max_length=1000, null=True, blank=True)
    publishedAt = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title