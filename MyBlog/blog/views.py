from django.shortcuts import render
from django.views.generic import CreateView
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import Profile
from django.contrib import messages

class CreateBlog(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'createBlog.html'
    model = Blog
    success_url = '/'

    def form_valid(self, form):

        instance = form.save(commit=False)
        instance.profile = Profile.objects.get(user=self.request.user)
        title = self.request.POST.get('title')
        blog_image = self.request.FILES.get('blog_image')
        
        if not title:
            # form.add_error(None,'This field is required')
            messages.error(self.request, "Title field is required")
            return self.form_invalid(form)

        if not blog_image:
            messages.error(self.request, "Blog image  is required")
            return self.form_invalid(form)
        
        instance.title = title
        instance.blog_image = blog_image
        instance.save()

        return super().form_valid(form)


    
