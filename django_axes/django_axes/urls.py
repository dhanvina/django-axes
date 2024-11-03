from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_axes_app.urls')),  # Include your app's URLs
]
