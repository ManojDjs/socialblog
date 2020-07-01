from .views import BlogpostCreate, BlogpostDetail, CommentCreate, CommentDetail, MessagesCreate,Postedit,Messageedit,PostCreate
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path(r'blogs/', BlogpostCreate.as_view(), name='blog-post'),
    path(r'blogs/<int:pk>/', BlogpostDetail.as_view(), name='blog-detail'),
    path(r'review/<int:pk>/', CommentDetail.as_view(), name='comment-create'),
    path(r'blogs/<int:pk>/review', CommentCreate.as_view(), name='comment-post'),
    path(r'blogs/message/', MessagesCreate.as_view(), name='message'),
    path(r'blogs/messagesearch/', MessagesCreate.as_view(), name='messagesearch'),
    path(r'blogs/message/<int:pk>', Messageedit.as_view(), name='message-edit'),
    path(r'blogs/post/', PostCreate.as_view(), name='post'),
path(r'blogs/post/<int:pk>', Postedit.as_view(), name='post-edit'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
