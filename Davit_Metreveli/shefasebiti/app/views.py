from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from .throttles import CustomPostThrottle


class PostListView(APIView):
    throttle_scope = 'posts_list'

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostCreateView(APIView):
    throttle_scope = 'posts_create'
    throttle_classes = [CustomPostThrottle]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)