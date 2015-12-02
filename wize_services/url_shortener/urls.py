from django.conf.urls import url
from .views import UrlConvertView, UrlListView, UrlRedirectShortUrl

urlpatterns = [
    url(r'^convert_url/$', UrlConvertView.as_view(), name='convert_url'),
    url(r'^url_list/$', UrlListView.as_view(), name='url_list'),
    url(r'^redirect_short_url/$', UrlRedirectShortUrl.as_view(), name='redirect_short_url'),

]
