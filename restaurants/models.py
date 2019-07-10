from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name= models.CharField(max_length=120)
	description=models.TextField()
	opening_time=models.DateTimeField(auto_now_add=False)
	closing_time=models.DateTimeField(auto_now_add=False)
	def __str__(self):
		return self.name