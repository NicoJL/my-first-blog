from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='postdetail'),
	url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_post,name='add_comment_post'),
	url(r'^post/new/$', views.post_new,name='postnew'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit
		,name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/approve/$', views.comments_approve,name='comments_approve'),
	url(r'^post/(?P<pk>[0-9]+)/remove/$', views.comments_remove,name='comments_remove'),
]