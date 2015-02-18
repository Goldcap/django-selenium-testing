from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
     url(r'^testing', 'selenium_tests.views.test', name='test'),
     url(r'^$', 'selenium_tests.views.home', name='home'),
     
    #GLOBALS
    url(r'^login/', 'selenium_tests.views.dologin', name="dologin"),
    url(r'^signup/', 'selenium_tests.views.signup', name="signup"),
    url(r'^pending/', 'selenium_tests.views.pending', name="pending"),
    url(r'^account/',include('django.contrib.auth.urls')),
    url(r'^forgot-password/$','selenium_tests.views.forgot_password',name="forgot-password"),
    url(r'^account/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
    {'next_page': '/login/'}),           
)