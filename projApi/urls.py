from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('watch/',include('apiApp.api.urls')),
    path('account/',include('user_app_auth.api.urls')),
]
    
