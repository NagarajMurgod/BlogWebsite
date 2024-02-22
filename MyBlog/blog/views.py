from django.shortcuts import render
from django.views.generic import CreateView
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateBlog(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'createBlog.html'
    # model = Blog
    # success_url = '/'
    
