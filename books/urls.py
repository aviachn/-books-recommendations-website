
from django.contrib import admin
from django.urls import re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'articles/', include('articles.urls')),
    re_path(r'accounts/', include('accounts.urls')),
    re_path(r'^$', views.homepage, name="home"),
]

urlpatterns += staticfiles_urlpatterns()                #the function check if we're in debug mode, and will append to urlpatterns so it will know how to serve our static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
