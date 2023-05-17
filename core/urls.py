from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tag', TagViewSet)
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('api/', include(router.urls)),

]
