from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog

class Homeview(TemplateView):

    template_name = 'home.html'





class TestView(LoginRequiredMixin,TemplateView):
    template_name = 'test.html'