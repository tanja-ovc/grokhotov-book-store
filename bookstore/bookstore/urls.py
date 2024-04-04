from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from books.api.v1.drf_yasg_integration import (
    DecoratedTokenObtainPairView, DecoratedTokenRefreshView
)

schema_view = get_schema_view(
   openapi.Info(
       title="Bookstore API",
       default_version='v1',
   ),
   url='http://localhost',
   public=True,
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/token/', DecoratedTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', DecoratedTokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/v1/books/', include('books.api.v1.urls')),
    path('feedback/', include('feedback.urls'))
]
