from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.conf.urls.static import static
 # New Import
from django.conf import settings

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/logoBox/'


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logoBox/', include('logoBox.urls')),
   # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)','serve', {'document_root': settings.MEDIA_ROOT}), )
