
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home/', include('Website.urls')),
    path('admin/', admin.site.urls),
]
