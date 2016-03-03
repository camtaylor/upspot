from django.conf.urls import  url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'spots', views.SpotViewSet)
urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
