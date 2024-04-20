from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Blog
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from .serializers import ProfileSerializer
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


User = get_user_model()


class ProfileApiView(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        profile = Profile.objects.get(user_id=self.request.user.id)
        return profile




class ProfileView(LoginRequiredMixin,ListView):
    template_name = 'userprofile.html'

    def get_context_data(self):
        context = super().get_context_data()
        user = Profile.objects.filter(user_id = self.request.user.id).first()
        context['profile_data'] = user
    
        return context


    def get_queryset(self):
        blogs = Blog.objects.filter(profile__user_id=self.request.user.id)
        return blogs


  



