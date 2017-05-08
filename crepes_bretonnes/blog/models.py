from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	author = models.CharField(max_length=42)
	content = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
	category = models.ForeignKey('Category')

	def __str__(self):
		return self.title