from django.shortcuts import render
from .serializers import *
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render,get_object_or_404

# Create your views here.
@api_view(['POST'])
def register(request):
	from rest_framework_jwt.settings import api_settings
	jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
	jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

	usr = None
	auth_usr = None
	if User.objects.filter(name=request.data["username"]).exists():
		return Response({"err_no":101,"msg":"duplciate username"}, status=status.HTTP_400_BAD_REQUEST)
	auth_usr = get_user_model().objects.create_user(username=request.data["username"],password=request.data["password"])
	usr = User.objects.create(name=request.data["username"],
			displayname=request.data["username"],
			avatar="",
			signature="",
			sex = "",
		)
	#auth_usr = get_user_model().objects.get(username=number)
	payload = jwt_payload_handler(auth_usr)
	resp = {'token':jwt_encode_handler(payload)}
	return Response(resp, status=status.HTTP_201_CREATED)


class UserList(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserBasicSerializer

class UserItem(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = "name"
	queryset = User.objects.all()
	serializer_class = UserBasicSerializer



