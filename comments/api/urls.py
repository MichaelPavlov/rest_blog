from django.conf.urls import url

from comments.api.views import CommentListAPIView, CommentDetailAPIView, CommentCreateAPIView

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name="list"),
    url(r'^create/$', CommentCreateAPIView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name="thread"),
    # url(r'^(?P<pk>\d+)/edit/$', CommentEditAPIView.as_view(), name="edit"),
]
