from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]

# Don't understand why code below was not working
# Figured it out -- need to use += to add to add a new mapping urlpatterns, or you can
# redeclare it in each step (like below), or you can state it all at once (like above)
# above is most efficient and most natural if you aren't going step by step through tutorial

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^books/$', views.BookListView.as_view(), name='books'),
# ]
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^books/$', views.BookListView.as_view(), name='books'),
#     url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
# ]
#
# urlpatterns += [
#     url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
# ]
#
# urlpatterns += [
#     url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
# ]
