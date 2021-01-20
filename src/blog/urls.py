from django.urls import path
from .views import CategoryListView, CommentCreateListView, PostCreateListView, PostViewCreateListView, LikeCreateListView, BadPostCreateListView, CommentLikeCreateListView, BadCommentCreateListView

urlpatterns = [
    path('category-list/', CategoryListView.as_view(), name="category-list"),
    path('comment/<slug>/', CommentCreateListView.as_view(), name="comment"),
    path('post/', PostCreateListView.as_view(), name="post"),
    path('post-view/<slug>/', PostViewCreateListView.as_view(), name="post-view"),
    path('like/<slug>/', LikeCreateListView.as_view(), name="like"),
    path('bad-post/<slug>/', BadPostCreateListView.as_view(), name="bad-post"),
    path('comment-like/<id>/', CommentLikeCreateListView.as_view(), name="comment-like"),
    path('bad-comment/<id>/', BadCommentCreateListView.as_view(), name="bad-comment"),
]
