from django.urls import path
from .views import profile_add_anime, profile_delete_anime

urlpatterns = [
    path('anime/<int:pk>/add', profile_add_anime, name='add'),
    path('anime/<int:pk>/delete', profile_delete_anime, name='delete'),
]
