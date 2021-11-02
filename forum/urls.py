from . import views
from django.urls import path


urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('add-post/', views.Add_Post.as_view(), name='add-post'),
    path('article/<int:pk>/', views.PostView.as_view(), name='postview'),
    path('like/<int:pk>', views.LikeView, name='post_like'),
    path('<str:name>/', views.PostList.as_view(), name='postlist'),
]