"""proc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import registration.backends.default.urls

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from core.views import CustomRegistrationView, router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',
        CustomRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/', include(registration.backends.default.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
if settings.MEDIA_URL:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
