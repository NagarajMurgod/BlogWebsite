from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Blog
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from .serializers import ProfileSerializer
from .models import Profile


User = get_user_model()


class ProfileApiView(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        profile = Profile.objects.get(user_id=self.request.user.id)
        return profile


class ProfileView(ListView):

    def get_queryset(self):

        blogs = Blog.objects.filter(profile__user_id=self.request.user.id)
        print(blogs)
        return blogs


    template_name = 'userprofile.html'



