from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=50)
	year = models.IntegerField(default="0")
	description = models.CharField(max_length=300)
	genre = models.CharField(max_length=30)
	runtime = models.CharField(max_length=10)
	language = models.CharField(max_length=20)
	country = models.CharField(max_length=30)
	actors = models.CharField(max_length=300)
	image = models.ImageField(upload_to='')
	avg_rating = models.DecimalField(max_digits=3, decimal_places=1, default="5")
	
class Rating(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
	rating = models.IntegerField(default=5)

class WishList(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE)
	movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
