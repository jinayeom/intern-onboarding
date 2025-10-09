from django.db import models

class Topic(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)  # markdown or html

    def __str__(self):
        return self.title
