from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileView(ListView):

    def get_queryset(self):

        blogs = Blog.objects.filter(profile__user_id=self.request.user.id)
        print(blogs)
        return blogs


    template_name = 'userprofile.html'
