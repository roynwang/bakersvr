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
	material_detail = MaterialSerializer(read_only=True)
	class Meta:
		model = RecipeMaterial

class StepSerializer(serializers.ModelSerializer):
	class Meta:
		model = Step

class RecipeDetailSerializer(serializers.ModelSerializer):
	author = UserBasicSerializer(read_only=True)
	materials = RecipeMaterialSerializer(many=True, read_only=True)
	steps = StepSerializer(many=True,read_only=True)
	class Meta:
		model = Recipe

class CommentSimpleSerializer(serializers.ModelSerializer):
	by_detail = UserBasicSerializer(read_only=True, source="by")
	class Meta:
		model = Comment

class CommentSerializer(serializers.ModelSerializer):
	reply_to_detail = CommentSimpleSerializer(read_only=True, source="reply_to")
	by_detail = UserBasicSerializer(read_only=True, source="by")
	class Meta:
		model = Comment

class CategeorySimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categeory

class CategeorySerializer(serializers.ModelSerializer):
	recipe_set = RecipeBasicSerializer(read_only=True, many=True)
	class Meta:
		model = Categeory

class BannerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Banner

