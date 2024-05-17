from rest_framework.generics import ListAPIView
from blog.serializers import BlogSerializer
from blog.models import Blog,Categories


class UserBLogApiView(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        blogs = Blog.objects.filter(profile__user_id=self.request.user.id)
        return blogs