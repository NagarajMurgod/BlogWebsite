from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Blog
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from .serializers import ProfileSerializer
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.serializers import BlogSerializer

User = get_user_model()


class ProfileApiView(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user_id=self.request.user.id)
            return profile
        return None




class ProfileView(LoginRequiredMixin,ListView):
    template_name = 'userprofile.html'
    context_object_name = 'blogs'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = Profile.objects.filter(user_id = self.request.user.id).first()
        user_details = {
            'name' : user.name,
            'profile_img': user.profile_img.url,
            'bio' : user.bio
        }
        print(user_details)
        context['profile_data'] = user_details
        return context


    def get_queryset(self):
        blogs = Blog.objects.filter(profile__user_id=self.request.user.id)
        return blogs

  



