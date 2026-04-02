# api/schema.py

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="University Advisor API",
        default_version='v1',
        description="""
        API documentation for University Advisor platform.
        
        This API provides endpoints for:
        - User authentication and profiles
        - Major recommendations and comparisons
        - AI-powered career advising
        - Course and book recommendations
        
        ## Authentication
        Most endpoints require authentication using JWT tokens.
        
        ## Rate Limiting
        API is rate limited to 100 requests per minute per user.
        
        ## Error Codes
        - 400: Bad Request
        - 401: Unauthorized
        - 403: Forbidden
        - 404: Not Found
        - 500: Internal Server Error
        """,
        terms_of_service="https://www.university-advisor.com/terms/",
        contact=openapi.Contact(email="api@university-advisor.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]