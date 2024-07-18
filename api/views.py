from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializers import *

class PostView(APIView):
    def get(self, request):
        output = [
            {
                'title': output.title,
                'description': output.description,
                'author': output.author,
                'pub_date': output.pub_date,
            } 
            for output in Post.objects.all()
        ]
        return Response(output)
        
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class PatternView(APIView):
    def get(self, request):
        output = [
            {
                'title': output.title,
                'instructions': output.instructions,
                'description': output.description,
                'author': output.author,
                'pub_date': output.pub_date,
            } 
            for output in Pattern.objects.all()
        ]
        return Response(output)
    def post(self,request):
        serializer = PatternSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class InspirationView(APIView):
    def get(self, request):
        output = [
            {
                'title': output.title,
                'insp_link': output.insp_link,
                'seeking_pattern': output.seeking_pattern,
                'description': output.description,
                'author': output.author,
                'pub_date': output.pub_date,

            } 
            for output in Inspiration.objects.all()
        ]
        return Response(output)
    def post(self,request):
        serializer = InspirationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
