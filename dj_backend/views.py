from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class UserProfileView(TemplateView):
    template_name = 'user-profile.html'


class RegisterView(TemplateView):
    template_name = 'register.html'
