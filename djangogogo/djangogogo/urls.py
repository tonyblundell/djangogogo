from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

uid_regex = '(?P<uidb64>[0-9A-Za-z_\-]+)'
token_regex = '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangogogo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$',
        TemplateView.as_view(template_name='index.html'),
        name='index'),
)
