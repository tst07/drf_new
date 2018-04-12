# base/router.py
from . import views
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()

# router.register(r'banks', views.BankViewSet)

api_urlpatterns = router.urls
