from django.contrib import admin
from django.urls import path,include,re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authentication.urls')),
    path('',include('pm.urls')),
    re_path(r'^\.well-known/', include('letsencrypt.urls'))
]
