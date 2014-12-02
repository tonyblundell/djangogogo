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
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^accounts/password-change/$',
        'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^accounts/password-change/done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
    url(r'^accounts/password-reset/$',
        'django.contrib.auth.views.password_reset',
        name='password_reset'),
    url(r'^accounts/password-reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),
    url(r'^accounts/password-reset/{0}/{1}/$'.format(uid_regex, token_regex),
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^accounts/reset/done/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
    url(r'^about/',
        TemplateView.as_view(template_name='index.html'),
        name='index'),
)
