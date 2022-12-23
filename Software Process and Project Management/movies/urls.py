from django.conf.urls import url

from . import views

app_name = 'movies'
urlpatterns = [
	url(r'^$', views.listing, name='index'),
	url(r'^wishlist/(?P<user_id>[0-9]+)/$', views.show_wish_list, name='wishlist'),
	url(r'^remove-wishlist/$', views.remove_from_wish_list, name='remove-wishlist'),
	url(r'^add-wishlist/$', views.add_to_wish_list, name='add-wishlist'),
	url(r'^rate/$', views.rate, name='rate'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^update/(?P<user_id>[0-9]+)/$', views.update, name='update'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
]