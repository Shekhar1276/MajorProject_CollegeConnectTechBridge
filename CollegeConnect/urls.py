# CollegeConnect/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('user.urls')), 
    path('social/', include('social.urls')),
    path('career/', include('career.urls')),
    path('blogs/', include('blogs.urls')),


    # Add more URL patterns for other apps if needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
