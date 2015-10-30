from django.conf.urls import patterns, url,include
from recipe.views import *

urlpatterns = patterns('',
        url(r'^api/user/(?P<name>[a-zA-Z0-9]{4,20})/myrecipe/$', MyRecipeList.as_view()),
        url(r'^api/user/(?P<name>[a-zA-Z0-9]{4,20})/bookmark/$', MyFavList.as_view()),
		url(r'^api/recipe/(?P<pk>[0-9]+)/$', RecipeItem.as_view()),
		url(r'^api/recipe/(?P<pk>[0-9]+)/comments/$', RecipeCommentList.as_view()),
		url(r'^api/recipe/$', RecipeList.as_view()),
		url(r'^api/categeory/$', CateList.as_view()),
		url(r'^api/categeory/(?P<pk>[0-9]+)/$', CateItem.as_view()),
		url(r'^api/banner/$', BannerList.as_view()),
		url(r'^api/banner/(?P<pk>[0-9]+)/$', BannerItem.as_view()),
		url(r'^api/private/material/$', MaterialList.as_view()),
		url(r'^api/private/recipematerial/$', RecipeMaterialList.as_view()),
		url(r'^api/private/step/$',StepList.as_view()),
		)

