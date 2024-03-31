from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class AppMain(ListView, LoginRequiredMixin):
    model = Name_of_game
    template_name = 'main_page.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Name_of_game.objects.all()
