from django.shortcuts import render
from .models import Anime
import requests
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)


def data_api():
    url = f'https://api.jikan.moe/v4/anime'
    r = requests.get(url)
    data = r.json()
    return data['data']


def import_data(data):
    for result in data:
        # get all values from list(genres) of dictionary with key 'name'
        result_genres = [g['name'] for g in result['genres']]

        anime = Anime(title=result['title'],
                      anime_type=result['type'],
                      episodes=result['episodes'],
                      status=result['status'],
                      aired=result['aired']['string'],
                      image=result['images']['jpg']['image_url'],
                      synopsis=result['synopsis'],
                      rating=result['rating'],
                      score=result['score'],
                      genres=result_genres)
        anime.save()


class AnimeListView(ListView):
    model = Anime
    paginate_by = 8
    context_object_name = 'anime_list'
    ordering = ['-score']

    # data = data_api()
    # import_data(data)


class AnimeDetailView(DetailView):
    model = Anime


class AnimeCreateView(LoginRequiredMixin, CreateView):
    model = Anime
    fields = ['title', 'anime_type', 'score']
    permission_required = 'is_staff'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class AnimeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Anime
    fields = ['title', 'anime_type', 'score']
    permission_required = 'is_staff'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # anime = self.get_object()
        if self.request.user.is_staff:
            return True
        else:
            return False


class AnimeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Anime
    success_url = '/'
    permission_required = 'is_staff'

    def test_func(self):
        # anime = self.get_object()
        if self.request.user.is_staff:
            return True
        else:
            return False
