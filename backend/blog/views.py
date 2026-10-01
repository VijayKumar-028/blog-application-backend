from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer

# Create your views here.

#below are the function based CRUD Operations

# @api_view(['GET', 'POST'])
# def post_list(request):
#     if request.method=='GET':
#         posts=Post.objects.all()
#         serializer=PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     elif request.method=='POST':
#         serializer=PostSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)

#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def post_detail(request,pk):
#     if request.method=='GET':
#         post=get_object_or_404(Post, pk=pk)
#         serializer=PostSerializer(post)
#         return Response(serializer.data)

#     elif request.method=='PUT':
#         post=get_object_or_404(Post, pk=pk)

#         serializer=PostSerializer(post, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)

#     elif request.method=='PATCH':
#         post=get_object_or_404(Post, pk=pk)
        
#         serializer=PostSerializer(post, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)

#     elif request.method=='DELETE':
#         post=get_object_or_404(Post, pk=pk)

#         post.delete()

#         return Response(status=204)

# Class based using ModelViewSet
class PostViewSet(ModelViewSet):
    
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields=['category']
    search_fields=['title', 'content', 'category__name']
    ordering_fields=['created_at', 'title']
    queryset=Post.objects.select_related('category').prefetch_related('comments')
    serializer_class=PostSerializer