from django.db import models


class Article(models.Model):
    article_title = models.CharField(name='article title', max_length=50)
    name_poster = models.CharField(name='name poster', max_length=50)
    article_text = models.TextField(name='article text', max_length=255)
