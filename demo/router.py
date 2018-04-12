# base/router.py
from . import views
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()

router.register(r'banks', views.BankViewSet)
router.register(r'branches', views.BranchViewSet)
router.register(r'accounts', views.AccountsViewSet)
router.register(r'customers', views.CustomerViewSet)

api_urlpatterns = router.urls
