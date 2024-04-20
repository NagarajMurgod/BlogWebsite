from django.contrib import admin
from .models import Blog, Categories,CategoryBlog
# Register your models here.

admin.site.register(Blog)
admin.site.register(Categories)
admin.site.register(CategoryBlog)
