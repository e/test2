from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from resolutions import views as resolution_views
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    url(r'^testlivesmart/admin/', admin.site.urls),
    url(r'^testlivesmart/login/$', auth_views.login, {
        'template_name': 'login.html'}, name='login'),
    url(r'^testlivesmart/logout/$', auth_views.logout, name="logout",),
    url(r'^testlivesmart/$', resolution_views.Home.as_view(), name="home"),
    url(r'^testlivesmart/accounts/password/reset/$',
        auth_views.password_reset,
        {'post_reset_redirect' : '/testlivesmart/accounts/password/reset/done/',
         'template_name' : 'password_reset.html'},
        name="password_reset"),
    url(r'^testlivesmart/accounts/password/reset/done/$',
        auth_views.password_reset_done,
        {'template_name' : 'password_reset_done.html'},
        name='password_reset_done'),
    url(r'^testlivesmart/accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {'post_reset_redirect' : '/testlivesmart/accounts/password/done/',
         'template_name': 'password_reset_form.html'},
        name="password_reset_confirm"),
    url(r'^testlivesmart/accounts/password/done/$',
        auth_views.password_reset_complete,
        {'template_name': 'password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^testlivesmart/accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^testlivesmart/api/', include('resolutions.api_urls', namespace='api')),
    url(r'^testlivesmart/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^testlivesmart/api-token-auth/', authtoken_views.obtain_auth_token)
]
