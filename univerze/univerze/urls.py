"""
URL configuration for univerze project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from core import views as core_views
from gallery import views as gallery_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('gallery', gallery_views.gallery, name="gallery"),
    path('news', core_views.news, name="news"),
    path('contact', core_views.contact, name="contact"),
    path('event', core_views.event, name="event"),
    path('planets', core_views.planets, name="planets"),
    path('notices', core_views.notices, name="notices"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)