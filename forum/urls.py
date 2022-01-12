from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('article/<int:pk>/delete', views.Delete_Post.as_view(), name='delete_post'),
    path('article/<int:id>/', views.PostView.as_view(), name='postview'),
    path('like/<int:id>', views.LikeView, name='post_like'),
    path('<str:name>/', views.PostList.as_view(), name='postlist'),
    path('<str:game>/add-post/', views.Add_Post.as_view(), name='add-post'),
    path('accounts/', include('allauth.urls')),
    path('article/<int:id>/add_comment', views.Add_Comment.as_view(), name='add_comment'),
    path('article/<int:pk>/delete_comment', views.Delete_Comment.as_view(), name='delete_comment'),
]
