from django.db import models

# Create your models here.
class Chismes(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=50, default="buen chisme")
