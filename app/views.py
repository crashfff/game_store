from itertools import chain
import numpy as np
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import RegisterUserForm
from .models import *


class AppMain(ListView, LoginRequiredMixin):
    model = Name_of_game
    template_name = 'main_page.html'
    context_object_name = 'games'

    def get_queryset(self):
        queryset = Name_of_game.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queryset1'] = Name_of_game.objects.order_by('quantity_purchased').reverse
        return context

@login_required
def profile_view(request):
    return render(request, 'profile.html')

def logout_user(request):
    logout(request)

    return redirect('main_page')


class DataMixin:
    pass


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)


        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')
