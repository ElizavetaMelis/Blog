from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.comment.views import CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView, \
    AnswerViewSet

router = DefaultRouter()
router.register('answers', AnswerViewSet)


urlpatterns = [
    path('comment-create/', CommentCreateView.as_view()),
    path('comment-list/', CommentListView.as_view()),
    path('comment-update/<int:pk>/', CommentUpdateView.as_view()),
    path('comment-delete/<int:pk>/', CommentDeleteView.as_view()),
    path('', include(router.urls))
]
