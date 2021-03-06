from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json
from random import randint
from smsverify.models import *
from usr.models import *
from .serializers import *
from django.contrib.auth import get_user_model

import base64
import datetime
import urllib2
import md5
from django.conf import settings

class SMSGet(generics.CreateAPIView):
	pagination_class = None
	queryset = Sms.objects.all()
	serializer_class = SmsVcodeSerializer 
	def create(self, request, *args, **kwargs):
		vcode = randint(100000,999999)
		num, _ =  Sms.objects.get_or_create(number=request.DATA["number"])
		num.vcode = vcode
		num.save()
		resp = templateSMS(settings.UCPAASSID,
				settings.UCPAASTOKEN,
				settings.UCPAASAPPID,
				num.number,
				settings.UCPAASTEMPLATE,
				str(vcode) + "," + "2")

		print resp
		serializer = SmsVcodeSerializer(num)
		return Response(serializer.data, status=status.HTTP_200_OK)

class SMSVerify(APIView):

	def get_or_create_user_return_token(self, number):
		from rest_framework_jwt.settings import api_settings
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
	
		try:
			usr = User.objects.get(name=number)
		except:
			usr = None
		auth_usr = None
		if not usr:
			auth_usr = get_user_model().objects.create_user(username=number,password=str(randint(100000,999999)))
			usr = User.objects.create(name=number,
					displayname=number,
					avatar=settings.DEFAULT_AVATAR
					)
			#create timeline and working hours

		else: 
			auth_usr = get_user_model().objects.get(username=number)
		payload = jwt_payload_handler(auth_usr)
		return {'token':jwt_encode_handler(payload)}

	
	def get(self,request,number):
		sms = get_object_or_404(Sms,number=number)
		ret = None
		print request.GET
		if str(sms.vcode) == request.GET["vcode"]:
			#ret = Response(self.get_or_create_user_return_token(number) , status=status.HTTP_200_OK)
			ret = Response({"result":"success"}, status=status.HTTP_200_OK)
			#generate token
			sms.vcode = randint(100000,999999)
			sms.save()
		else:
			ret = Response({"result":"failed"}, status=status.HTTP_403_FORBIDDEN)
		
		return ret


def getSig(accountSid,accountToken,timestamp):
	sig = accountSid + accountToken + timestamp
	return md5.new(sig).hexdigest().upper()

def getAuth(accountSid,timestamp):
	src = accountSid + ":" + timestamp
	return base64.encodestring(src).strip()

def urlOpen(req,data=None):
	try:
		res = urllib2.urlopen(req,data)
		data = res.read()
		res.close()
	except urllib2.HTTPError, error:
		data = error.read()
		error.close()
	return data

def createHttpReq(req,url,accountSid,timestamp,responseMode,body):
	req.add_header("Authorization", getAuth(accountSid,timestamp))
	print "Auth:"
	print getAuth(accountSid, timestamp)
	if responseMode:
		req.add_header("Accept","application/"+responseMode)
		req.add_header("Content-Type","application/"+responseMode+";charset=utf-8")
	if body:
		req.add_header("Content-Length",len(body))
		req.add_data(body)
	print req
	return req

def templateSMS(accountSid,accountToken,appId,toNumbers,templateId,param,isUseJson=True):
	now = datetime.datetime.now()
	timestamp = now.strftime("%Y%m%d%H%M%S")
	signature = getSig(accountSid,accountToken,timestamp)
	url = settings.UCPAASHOST + ":" + settings.UCPAASPORT + "/" + settings.UCPAASSOFTVER + "/Accounts/" + accountSid + "/Messages/templateSMS?sig=" + signature
	print url
	if isUseJson == True:
		body = '{"templateSMS":{ "appId":"%s","to":"%s","templateId":"%s","param":"%s"}}'%(appId,toNumbers,templateId,param)
		print body
		responseMode = "json"
	else:
		body = "<?xml version='1.0' encoding='utf-8'?>\
				<templateSMS>\
				<appId>%s</appId>\
				<to>%s</to>\
				<templateId>%s</templateId>\
				<param>%s</param>\
				</templateSMS>\
				"%(appId,toNumbers,templateId,param)
		responseMode = "xml"
	req = urllib2.Request(url)
	return urlOpen(createHttpReq(req,url,accountSid,timestamp,responseMode,body))
