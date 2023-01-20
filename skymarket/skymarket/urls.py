from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/", include('ads.urls')),
    path('api/token/', include('djoser.urls')),
    path('api/token/', include('djoser.urls.jwt')),
    path(r'api/', include('djoser.urls.authtoken')),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/shema/", SpectacularAPIView.as_view(),name='schema'),
    path("api/shema/swagger-ui/", SpectacularSwaggerView.as_view(url_name= 'schema'),name='swagger-ui'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)