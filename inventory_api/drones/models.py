# drones/models.py
from django.db import models
from django.contrib.auth.models import User


# create Model for Drones Database
class Drones(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	model = models.CharField(max_length=50)
	megapixel = models.IntegerField()
	brand = models.CharField(max_length=50)
	serialno = models.CharField(max_length=50)
	supported_cameras = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.serialno