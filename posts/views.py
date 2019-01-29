from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
