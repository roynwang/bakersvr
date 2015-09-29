from django.conf.urls import patterns, url,include
from recipe.views import *

urlpatterns = patterns('',
		url(r'^api/recipe/(?P<pk>[0-9]+)/$', RecipeItem.as_view()),
		url(r'^api/recipe/(?P<pk>[0-9]+)/comments/$', RecipeCommentList.as_view()),
		url(r'^api/recipe/$', RecipeList.as_view()),
		url(r'^api/private/material/$', MaterialList.as_view()),
		url(r'^api/private/recipematerial/$', RecipeMaterialList.as_view()),
		url(r'^api/private/step/$',StepList.as_view()),
		)

