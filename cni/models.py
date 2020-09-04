from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
	title = models.CharField(max_length=100)
	overview = models.TextField()
	thumbnail = models.ImageField()
	featured = models.BooleanField()

	def __str__(self):
		return self.title

