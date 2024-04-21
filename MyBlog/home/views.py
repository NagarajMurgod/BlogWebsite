from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog,Categories

<<<<<<< HEAD
class Homeview(ListView):
=======
class Homeview(LoginRequiredMixin, ListView):
>>>>>>> f3e639127bc8bd9ab3d7ade583653d190f736d67

    template_name = 'home.html'

    def get_queryset(self):
        queryset = Categories.objects.all()

        return queryset


<<<<<<< HEAD
=======



>>>>>>> f3e639127bc8bd9ab3d7ade583653d190f736d67
class TestView(LoginRequiredMixin,TemplateView):
    template_name = 'test.html'