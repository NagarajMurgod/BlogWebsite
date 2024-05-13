
from rest_framework.generics import ListAPIView
from blog.serializers import BlogSerializer
from blog.models import Blog,Categories


class CategoryBLogApiView(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        category = Categories.objects.get(category_name=self.kwargs['category'])
        blogs = Blog.objects.filter(categories=category)

        return blogs