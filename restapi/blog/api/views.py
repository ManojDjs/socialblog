from .serializers import BlogpostSerializer, CommentSerializer,MessagesSerializer,PostSerializer
from blog.models import Blogpost, Comment,Messages,Posts
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import filters
from rest_framework.filters import SearchFilter,OrderingFilter


class MessagesCreate(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['time','sender__username','receiver__username']
    def perform_create(self, serializer):
        sender=self.request.user
        serializer.save(sender=sender)
class PostCreate(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['text','author__username']
    def perform_create(self, serializer):
        sender=self.request.user
        serializer.save(author=sender)

class BlogpostCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer


class BlogpostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer
    lookup_field = 'pk'


class CommentCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('pk')
        post = get_object_or_404(Blogpost,pk=post_pk)
        serializer.save(post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
class Messagesearch(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    filter_backends = [SearchFilter]
    search_fields=('receiver','sender','text')
class Messageedit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    lookup_field = 'pk'
class Postedit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'



