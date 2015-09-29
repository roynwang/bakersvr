from django.shortcuts import render
from .serializers import *
from rest_framework import generics
# Create your views here.

class UserList(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserBasicSerializer

class UserItem(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = "name"
	queryset = User.objects.all()
	serializer_class = UserBasicSerializer

