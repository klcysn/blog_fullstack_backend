from django.urls import path
from .views import CategoryListView, CommentCreateListView, PostCreateListView, PostViewCreateListView, LikeCreateListView, BadPostCreateListView, CommentLikeCreateListView, BadCommentCreateListView, PostDetailCreateListView, CommentDetailView, LikeDetailView, CommentLikeDetailView, BadPostDetailView, BadCommentDetailView

urlpatterns = [
    path('category-list/', CategoryListView.as_view(), name="category-list"),
    path('comment/<slug>/', CommentCreateListView.as_view(), name="comment"),
    path('comment-detail/<slug>/<pk>/', CommentDetailView.as_view(), name="comment-detail"),
    path('post/', PostCreateListView.as_view(), name="post"),
    path('post-detail/<slug>/', PostDetailCreateListView.as_view(), name="post-detail"),
    path('post-view/<slug>/', PostViewCreateListView.as_view(), name="post-view"),
    path('like/<slug>/', LikeCreateListView.as_view(), name="like"),
    path('like-detail/<slug>/<pk>/', LikeDetailView.as_view(), name="like-detail"),
    path('bad-post/<slug>/', BadPostCreateListView.as_view(), name="bad-post"),
    path('bad-post-detail/<slug>/<pk>/', BadPostDetailView.as_view(), name="bad-post-detail"),
    path('comment-like/<slug>/<commentpk>/', CommentLikeCreateListView.as_view(), name="comment-like"),
    path('comment-like-detail/<slug>/<commentpk>/<pk>/', CommentLikeDetailView.as_view(), name="comment-detail-like"),
    path('bad-commentwarning/<slug>/<commentpk>/', BadCommentCreateListView.as_view(), name="bad-comment"),
    path('bad-commentwarning-detail/<slug>/<commentpk>/<pk>/', BadCommentDetailView.as_view(), name="bad-comment-detail"),
]
