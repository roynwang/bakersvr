from django.db import models

# Create your models here.

#for verify 
class VCode(models.Model):
	id = models.AutoField(primary_key=True)
	number = models.BigIntegerField(unique=True)

class User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, db_index=True, unique=True)
	avatar = models.CharField(max_length=256)
	signature = models.CharField(max_length=256)
	created = models.DateTimeField(auto_now=True)
	sex = models.CharField(max_length=32)
	def __unicode__(self):
		return self.name
