from django.shortcuts import render,get_object_or_404
# Create your views here.

from .serializers import *
from rest_framework import generics
from usr.models import *


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

class MyRecipeList(generics.ListAPIView):
	serializer_class = RecipeBasicSerializer
	def get_queryset(self):
		usr = get_object_or_404(User, name=self.kwargs.get("name"))
		return Recipe.objects.filter(author = usr.id)

class MyFavList(generics.ListAPIView):
	serializer_class = RecipeBasicSerializer
	def get_queryset(self):
		usr = get_object_or_404(User, name=self.kwargs.get("name"))
		#return Recipe.objects.filter(bookmark_by__contains = usr.id)
		return usr.bookmarks

class CateList(generics.ListCreateAPIView):
	serializer_class = CategeorySimpleSerializer 
	queryset = Categeory.objects.all()
	pagination_class = None
	
class CateItem(generics.ListAPIView):
	serializer_class = RecipeBasicSerializer
	def get_queryset(self):
		return get_object_or_404(Categeory, pk=self.kwargs.get("pk")).recipe_set
	

class BannerList(generics.ListCreateAPIView):
	serializer_class = BannerSerializer 
	queryset = Banner.objects.all()
	pagination_class = None
