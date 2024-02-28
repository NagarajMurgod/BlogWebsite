from rest_framework import serializers
from .models import Blog
from user.serializers import ProfileSerializer

class BlogSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Blog
        fields = [
            'title',
            'content',
            'blog_image',
            'created_at',
            'profile'
        ]

    def to_representation(self, instance):
        sd = super().to_representation(instance)
        sd['content'] = sd['content'][:400]+'...'
        return sd