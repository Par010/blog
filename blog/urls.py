from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from accounts.views import (login_view, register_view, logout_view)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls" , namespace='posts')),
    url(r'^comments/', include("comments.urls" , namespace='comments')),
    url(r'^login/', login_view, name="login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
