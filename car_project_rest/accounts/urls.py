from django.urls import path, include
from rest_framework import routers

from car_project_rest.accounts.views import RegisterViewSet, LoginView

router = routers.DefaultRouter()

router.register(r'register', RegisterViewSet, 'register')

urlpatterns = (
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls))
)

