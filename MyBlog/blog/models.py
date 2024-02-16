from django.db import models
from froala_editor.fields import FroalaField
from common.models import BaseModel
from profile.models import Profile

class BlogModel(BaseModel):
    title = models.CharField(max_length=255,related_name='blog')
    content = FroalaField()
    slug = models.SlugField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='blog/blog_images/')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='blogs')


    def __str__(self):
        return f"{slug}"


class CategoryBlog(BaseModel):
    ...


class Categories(BaseModel):
    category_name = models.CharField(max_length=150)

    def clean(self):
        self.category_name = self.category_name.lower()
        super().clean()
    
    def save(self,*args,**kwargs):
        self.full_clean()
        return super().save(*args,**kwargs)
    