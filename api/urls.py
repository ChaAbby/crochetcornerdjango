from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('post/', views.PostView.as_view(), name='post_view'),
    path('pattern/', views.PatternView.as_view(), name='pattern_view'),
    path('inspiration/', views.InspirationView.as_view(), name='inspiration_view')
]