"""myblog URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^aboutme/$', views.aboutme, name='aboutme'),
    url(r'^category/$', views.category, name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category_detail, name='category_detail'),
    url(r'^paper/(?P<paper_id>[0-9]+)/$', views.paper_detail, name='paper'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^archive/(?P<created_year>[0-9]+)/(?P<created_month>[0-9]+)/$', views.archive_detail, name='archive_detail'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tags, name='tag'),
]
#append url('media/' ) route. MEDIA_URL=/media/,MEDIA_ROOT=/home/czw/MyFirstBlog/media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



