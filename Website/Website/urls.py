
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myWebsite.urls')),
    path('login/', include('myWebsite.urls')),
    path('admin/', admin.site.urls),
]
