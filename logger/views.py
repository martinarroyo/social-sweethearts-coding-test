from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'logger/index.html'

class ProfileView(TemplateView):
    template_name = 'logger/profile.html'