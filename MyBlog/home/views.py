from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog,Categories

class Homeview(LoginRequiredMixin, ListView):

    template_name = 'home.html'

    def get_queryset(self):
        queryset = Categories.objects.all()

        return queryset





class TestView(LoginRequiredMixin,TemplateView):
    template_name = 'test.html'