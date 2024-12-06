from django.urls import path, include
from rest_framework_nested import routers
from .views import *

# api_router = routers.DefaultRouter()
api_router = routers.SimpleRouter()
api_router.register(r"articles", ArticleViewSet, basename="articles")

articles_router = routers.NestedSimpleRouter(api_router, r"articles", lookup="article")
articles_router.register(r"comments", CommentViewSet, basename="article-comments")

urlpatterns = [
    path("", include(api_router.urls)),
    path("", include(articles_router.urls)),
]

