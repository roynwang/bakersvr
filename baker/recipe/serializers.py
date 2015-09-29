from rest_framework import serializers
from usr.serializers import *
from .models import *

class RecipeBasicSerializer(serializers.ModelSerializer):
	author_detail = UserBasicSerializer(source="author",read_only=True)
	class Meta:
		model = Recipe


class MaterialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Material

class RecipeMaterialSerializer(serializers.ModelSerializer):
	material = MaterialSerializer(read_only=True)
	class Meta:
		model = RecipeMaterial

class StepSerializer(serializers.ModelSerializer):
	class Meta:
		model = Step

class RecipeDetailSerializer(serializers.ModelSerializer):
	author = UserBasicSerializer(read_only=True)
	materials = RecipeMaterialSerializer(many=True)
	steps = StepSerializer(many=True)
	class Meta:
		model = Recipe

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment

