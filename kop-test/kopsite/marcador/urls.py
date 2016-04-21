from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
    url(r'^query/$', 'marcador.query.query_bookmark',name='marcador_query_bookmark'),
    url(r'^search/$', 'marcador.search.run_search',name='marcador_search_bookmark'),
]
