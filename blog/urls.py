from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/gold/$', views.view_gold, name='view_gold'),
	url(r'^gold_post/$', views.post_gold, name="post_gold"),
	url(r'^mine_gold/$', views.mine_gold, name="mine_gold")
]