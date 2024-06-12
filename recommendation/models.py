import ast
from django.db import models
from django.urls import reverse


class Anime(models.Model):
    title = models.CharField(max_length=100)
    anime_type = models.CharField(max_length=10)
    episodes = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=15)
    aired = models.CharField(max_length=100)
    image = models.TextField()
    synopsis = models.TextField()
    rating = models.CharField(max_length=100)
    score = models.FloatField()
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def strGenres(self):
        aList = ast.literal_eval(self.genres)
        return aList
    
    def get_absolute_url(self):
        return reverse('anime-detail', kwargs={"pk": self.pk})
    