from django.conf.urls import url, include
from rest_framework import routers
from resolutions import api as views

router = routers.DefaultRouter()
router.register(r'resolutions', views.ResolutionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
