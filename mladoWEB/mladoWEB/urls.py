from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('server/', include('mladoServer.urls')),
    path('', include('main.urls')),
]
