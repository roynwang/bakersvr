from django.shortcuts import render
# Create your views here.

from .serializers import *
from rest_framework import generics


class RecipeList(generics.ListCreateAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeBasicSerializer

class RecipeItem(generics.RetrieveUpdateDestroyAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeDetailSerializer

class MaterialList(generics.ListCreateAPIView):
	queryset = Material.objects.all()
	serializer_class = MaterialSerializer

class RecipeMaterialList(generics.ListCreateAPIView):
	pagination_class = None
	queryset = RecipeMaterial.objects.all()
	serializer_class = RecipeMaterialSerializer

class StepList(generics.ListCreateAPIView):
	pagination_class = None
	queryset = Step.objects.all()
	serializer_class =StepSerializer 

class RecipeCommentList(generics.ListCreateAPIView):
	serializer_class = CommentSerializer
	def get_queryset(self):
		recipeid = self.kwargs.get('pk')
		queryset = Comment.objects.filter(recipe=recipeid)
		return queryset

