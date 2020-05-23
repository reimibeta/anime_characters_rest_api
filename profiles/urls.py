from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
# router.register('login', views.LoginViewSet, basename='login')

urlpatterns = [
    url(r'', include(router.urls))
]