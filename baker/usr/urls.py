from django.conf.urls import patterns, url,include
from usr.views import *

urlpatterns = patterns('',
		#url(r'^api/n/',register),
		#url(r'^api/v/$','rest_framework_jwt.views.obtain_jwt_token'),
		#url(r'^api/t/', 'rest_framework_jwt.views.refresh_jwt_token'),
		url(r'^api/user/$', UserList.as_view()),
        url(r'^api/user/(?P<name>[a-zA-Z0-9]{4,20})/$', UserItem.as_view()),
		)

