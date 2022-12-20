# Core imports.
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

# Third-party imports.
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


router = DefaultRouter()

urlpatterns = (
    [
        path('admin/', admin.site.urls),
        path('', include('apps.blog.urls')),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('api_auth/', include('rest_framework.urls')),
        path('auth/', include('apps.account.urls')),
        path('router/', include(router.urls), name='router'),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
