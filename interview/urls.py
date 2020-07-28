from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from .settings.yasg import urlpatterns as doc_urls
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
    path('api/v1/', include('api.urls'))
]

urlpatterns += doc_urls
urlpatterns += staticfiles_urlpatterns()
