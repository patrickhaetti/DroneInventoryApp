from django.contrib import admin
from django.urls import include, path 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('drones.urls')), # API endpoint
    path('api-auth/', include('rest_framework.urls')), # login on browsable API
]

