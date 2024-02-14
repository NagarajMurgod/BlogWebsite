from django.db import models
from froala_editor.fields import FroalaField


class BlogModel(models.Model):
    title = models.CharField(max_length=255,related_name='blog')
    content = FroalaField()
    slug = models.SlugField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='blog_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    