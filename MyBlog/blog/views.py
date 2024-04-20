from django.shortcuts import render
from django.views.generic import CreateView
from .forms import BlogForm
from .models import Blog,Categories
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import Profile
from django.contrib import messages
from rest_framework.generics import ListAPIView
from .serializers import BlogSerializer,CategorySerializer
from django.template.defaultfilters import slugify

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
        categories = self.request.POST.getlist('categories[]')
        
        if not title:
            # form.add_error(None,'This field is required')
            messages.error(self.request, "Title field is required")
            return self.form_invalid(form)

        if not blog_image:
            messages.error(self.request, "Blog image  is required")
            return self.form_invalid(form)
        
        instance.title = title
        instance.blog_image = blog_image
        instance.slug = slugify(title)
        instance.save()

        for cat in categories:
            if cat.isnumeric():
                obj = Categories.objects.get(id=int(cat))
            else:
                obj, _ = Categories.objects.get_or_create(category_name=cat.lower())
            instance.categories.add(obj)
        

        return super().form_valid(form)

    
class GetAllBlogsApiView(ListAPIView):
    
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer


class FilterBLogApiView(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        category = Categories.objects.get(id=self.kwargs['id'])
        blogs = Blog.objects.filter(categories=category)

        return blogs

class GetCategories(ListAPIView):
    
    serializer_class = CategorySerializer

    def get_queryset(self):
        term = self.request.GET.get('term')
        queryset = Categories.objects.filter(category_name__icontains = term)
        return queryset






    


    
