from rest_framework import serializers
from .models import Post, Pattern, Inspiration

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'author',
            'pub_date'
        ]

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = [
            'title',
            'instructions',
            'description',
            'author',
            'pub_date'
        ]

class InspirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspiration
        fields = [
            'title',
            'insp_link',
            'description',
            'author',
            'pub_date'
        ]