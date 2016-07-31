from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^$', views.api_root),
	url(r'^choferes/$',views.ChoferList.as_view(),name='chofer-list'),
	url(r'^choferes/(?P<pk>[0-9]+)/$',views.ChoferDetail.as_view(),name='chofer-detail'),
	url(r'^choferes/(?P<pk>[0-9]+)/highlight/$', views.ChoferHighlight.as_view(), name='chofer-highlight'),
	
	url(r'^users/$', views.UserList.as_view(),name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name='user-detail'),


	url(r'^test/$', views.testBusLog,name='test'),
]

urlpatterns = format_suffix_patterns(urlpatterns)