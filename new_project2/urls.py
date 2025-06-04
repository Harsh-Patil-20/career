from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finalapp.urls')), # Add this line to include your app's URLs
    # ... other project-level URL patterns ...
]