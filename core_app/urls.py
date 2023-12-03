"""
URL configuration for core_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from base_app.views import PictureDetail, PictureListView, image_upload, PictureList, DeletePicture

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_my_api/', include('rest_framework.urls')),
    path('test_api/<int:id>/', PictureDetail.as_view()),
    path('test_api/', PictureListView.as_view()),
    path('loading_picture/', image_upload, name='image_load'),
    path('list_picture/', PictureList.as_view()),
    path('remove_picture/<int:id>/', DeletePicture.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
