from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('snippets.views',
    url(r'^test/$', 'snippets_response'),
)

urlpatterns = format_suffix_patterns(urlpatterns)