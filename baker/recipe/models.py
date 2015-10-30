from django.db import models
from usr.models import *

# Create your models here.


class Material(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	buy_from = models.CharField(max_length=256)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name


class Recipe(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 64)
	introduction = models.CharField(max_length=1024)
	image = models.CharField(max_length=1024)
	up_by = models.ManyToManyField("usr.User", related_name="upped")
	bookmark_by = models.ManyToManyField("usr.User", related_name="bookmarks")
	author = models.ForeignKey("usr.User",related_name="my_post")
	created = models.DateTimeField(auto_now_add=True)
	recipe_cate = models.ForeignKey("Categeory", null=True)

	def __unicode__(self):
		return self.name

class RecipeMaterial(models.Model):
	id = models.AutoField(primary_key=True)
	material = models.ForeignKey(Material)
	recipe = models.ForeignKey(Recipe, related_name="materials")
	amount = models.CharField(max_length=64)

	def __unicode__(self):
		return self.material.name

class Step(models.Model):
	id = models.AutoField(primary_key=True)
	recipe = models.ForeignKey(Recipe, related_name="steps")
	image = models.CharField(max_length=1024)
	description = models.CharField(max_length=1024)
	voice = models.CharField(max_length=1024)
	section = models.IntegerField()
	def __unicode__(self):
		return self.recipe.name + " " + str(section)

class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	recipe = models.ForeignKey(Recipe, related_name="comments")
	by = models.ForeignKey("usr.User")
	comment = models.CharField(max_length=1024)
	reply_to = models.ForeignKey("self", null=True, blank=True, related_name="next_comment")
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.comment

class Categeory(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	pic = models.CharField(max_length=256)

class Banner(models.Model):
	id = models.AutoField(primary_key=True)
	url = models.CharField(max_length=512)
	pic = models.CharField(max_length=256)
	
