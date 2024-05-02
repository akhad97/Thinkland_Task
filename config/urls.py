from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
import debug_toolbar


schema_view = get_schema_view(
    openapi.Info(
    title="Swagger Doc for Test Proj",
    default_version='v1',
    description="This is Test Test project API",
    terms_of_service="example.uz",
    contact=openapi.Contact(email="example@gmail.com"),
    ),
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("main.apps.v1"), name="main"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui-v1"),
    path('__debug__', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


