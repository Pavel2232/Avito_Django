from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from ads.views import AdViewSet, CommentView

from ads.views import Ad_by_User

# TODO настройка роутов для модели
router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register('ads',AdViewSet)
comment_router = NestedSimpleRouter(router,
                                    r'ads',
                                    lookup='ad'
)
comment_router.register(r'comments',CommentView,basename='comments_ad')


urlpatterns = [
    path("ads/me/", Ad_by_User.as_view()),
    path("", include(comment_router.urls)),
    path("", include(router.urls)),

]
