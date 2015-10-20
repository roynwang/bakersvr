from rest_framework import serializers
from .models import *

class SmsVcodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sms
