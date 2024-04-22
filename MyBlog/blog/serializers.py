from rest_framework import serializers
from .models import Blog,Categories
from user.serializers import ProfileSerializer
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.html import strip_tags

class BlogSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Blog
        fields = [
            'title',
            'content',
            'blog_image',
            'created_at',
            'slug',
            'profile'
        ]

    def to_representation(self, instance):

        sd = super().to_representation(instance)
        sd['content'] = strip_tags(sd['content'])[:300]+'...'

        return sd


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'