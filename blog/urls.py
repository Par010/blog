
from django.conf.urls import url
from django.contrib import admin
from posts import views as posts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/$', posts_views.post_home),
]
