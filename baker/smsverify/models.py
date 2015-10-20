from django.db import models

# Create your models here.
class Sms(models.Model):
	id = models.AutoField(primary_key=True)
	number = models.CharField(max_length=32)
	vcode =  models.IntegerField(null=True)
