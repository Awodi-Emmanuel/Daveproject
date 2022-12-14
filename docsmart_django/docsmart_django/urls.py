"""docsmart_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="DocSmart APIs",
        default_version='v1',
        description="DocSmart VI APIs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@docsmart.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/faq/', include('faq.urls')),
    path('api/user/', include('user.urls')),
    path('api/company/', include('company.urls')),
    path('api/auth/', include('user_auth.urls')),
    path('api/documents/', include('documents.urls')),
    path('api/sales/', include('sales.urls')),
    path('api/customer/', include('customer.urls')),
    path('api/lines/', include('sale_lines.urls')),
    path('api/plugins/', include('plugins_base.urls')),
    path('api/billing/', include('billing.urls')),
    path('api/bankid/', include('bankid.urls')),
    url('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'mdeditor/', include('mdeditor.urls'))

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
