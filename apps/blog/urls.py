# Core imports.
from django.urls import path

# Local imports.
from core.urls import router
from .views import (
    PostView,
    PostsView,
    AddPostView,
    CategoryView,
    EditPostView,
    add_comment,
    get_comments,
    like_comment,
)
from .api import PostViewSet, CommentViewSet, CategoryViewSet


router.register(r'post_viewset', PostViewSet)
router.register(r'category_viewset', CategoryViewSet)
router.register(r'comment_viewset', CommentViewSet)

app_name = 'blog'

urlpatterns = [
    path('', PostsView.as_view(), name='home'),
    path('post/<slug:slug>/', PostView.as_view(), name='post'),
    path('category/<str:cat>/', CategoryView.as_view(), name='category'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit_post/<slug:slug>/', EditPostView.as_view(), name='edit_post'),
    path('add_comment/', add_comment, name='add_comment'),
    path('comment_like/', like_comment, name='like_comment'),
    path('get_comments/<slug:slug>/', get_comments, name='comments'),
]
