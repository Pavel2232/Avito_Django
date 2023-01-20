from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter
router = SimpleRouter()
router.register("users", UserViewSet, basename="users")

urlpatterns = [path('', include(router.urls)),
]
