"""
URL configuration for ckEditDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import re_path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from editer.views import index

urlpatterns = [
                  re_path(r'^admin/', admin.site.urls),
                  re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  re_path(r'^index/', index),  # 测试获取后台编辑的内容用的
                  path('ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  ## 没有这一句无法显示上传的图片
