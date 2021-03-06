"""adraft URL Configuration


"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from apps.notes.views import ListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/', ListView.as_view(), name='profile'),
    url(r'^', include('notes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
