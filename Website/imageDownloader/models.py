from django.db import models

class Image(models.Model):
	"""docstring for Image"""
	imgName = models.CharField(max_length=30)
