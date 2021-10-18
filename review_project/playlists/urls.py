from .views import PlaylistViewSet, PlaylistAddView, PlaylistRemoveView
from rest_framework.routers import DefaultRouter
from django.urls import path
# router.register('', PlaylistViewSet, basename='playlists')
# router.register('add.<str:pk>/add', PlaylistEstablishmentView, basename='add')
urlpatterns = [
    path('add/', PlaylistAddView.as_view(), name='add'),
    path('remove/', PlaylistRemoveView.as_view(), name='remove'),
    path('', PlaylistViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<str:pk>/', PlaylistViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),


]
