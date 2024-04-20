from django.db import models
from froala_editor.fields import FroalaField
from common.models import BaseModel
from user.models import Profile


class Categories(BaseModel):
    category_name = models.CharField(max_length=150)

    def clean(self):
        self.category_name = self.category_name.lower()
        super().clean()
    
    def save(self,*args,**kwargs):
        self.full_clean()
        return super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.category_name}"


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    content = FroalaField()
    slug = models.SlugField(max_length=255,null=True,blank=True, unique=True)
    blog_image = models.ImageField(upload_to='blog/blog_images/')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='blogs')
    description = models.CharField(max_length=255,default=" ")
    categories = models.ManyToManyField(Categories, through="CategoryBlog", related_name='blogs')


    def __str__(self):
        return f"{self.title}"


class CategoryBlog(BaseModel):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('blog_id', 'category_id'), name='blog_category'
            )
        ]


    


class Comments(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    comment_txt = models.TextField()



class BlogLikes(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                ['profile_id', 'blog_id'], name='blog_likes'
            )
        ]
