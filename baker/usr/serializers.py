from rest_framework import serializers
from usr.models import *
from django.contrib.auth import get_user_model

class VCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = VCode

class UserBasicSerializer(serializers.ModelSerializer):
	class Meta:
		model = User

