from rest_framework import serializers
from .models import Post, Pattern, Inspiration

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'description',
            'author',
            'pub_date'
        ]

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = [
            'instructions',
            'description',
            'author',
            'pub_date'
        ]

class InspirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspiration
        fields = [
            'insp_link',
            'seeking_pattern',
            'description',
            'author',
            'pub_date'
        ]