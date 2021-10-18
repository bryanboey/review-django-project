"""review_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import (
    RegisterView, LogOutView
)

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/token/refresh/', TokenRefreshView.as_view()),
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/logout/', LogOutView.as_view()),
    path('api/profiles/', include('users.urls')),
    path('api/establishments/', include('establishments.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/ratings/', include('ratings.urls')),
    path('api/playlists/', include('playlists.urls')),
    path('admin/', admin.site.urls),
]
