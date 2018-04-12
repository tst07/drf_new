from django.conf.urls import url, include
from . import views, router
from .router import api_urlpatterns as api_v1
from .v2.router import api_urlpatterns as api_v2

urlpatterns = [ 
    url(r'^v2/', include(api_v2, namespace="v2")),
	url(r'^(?P<version>(v1|v2))/', include(api_v1, namespace="v1")),
]
