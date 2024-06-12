# from pydoc import synopsis
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegister, UserUpadteForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from recommendation.models import Anime


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    anime_list = request.user.profile.anime_list.all()

    context = {
        'animeList': anime_list,
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpadteForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpadteForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_add_anime(request, pk):
    user_profile = request.user.profile
    anime = Anime.objects.filter(id=pk).first()

    if not user_profile.anime_list.filter(id=pk).exists():
        user_profile.anime_list.add(anime)
        messages.success(request, f'Dodano anime {anime} do twojej listy :D')

    return redirect(anime)


@login_required
def profile_delete_anime(request, pk):
    anime_list = request.user.profile.anime_list.all()
    user_profile = request.user.profile
    anime = user_profile.anime_list.filter(id=pk).first()
    user_profile.anime_list.remove(anime)

    context = {
        'animeList': anime_list,
    }
    return render(request, 'users/profile.html', context)
