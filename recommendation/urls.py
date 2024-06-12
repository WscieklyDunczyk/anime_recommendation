from django.urls import path
from .views import AnimeDeleteView, AnimeDetailView, AnimeListView, AnimeCreateView, AnimeUpdateView


urlpatterns = [
    path('', AnimeListView.as_view(), name='recommendation-home'),
    path('anime/<int:pk>/', AnimeDetailView.as_view(), name='anime-detail'),
    path('anime/new', AnimeCreateView.as_view(), name='anime-create'),
    path('anime/<int:pk>/update/', AnimeUpdateView.as_view(), name='anime-update'),
    path('anime/<int:pk>/delete/', AnimeDeleteView.as_view(), name='anime-delete'),
]
