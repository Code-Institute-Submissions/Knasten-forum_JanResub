from . import views
from django.urls import path


urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('<str:name>/', views.PostList.as_view(), name='postlist'),
    path('article/<int:pk>/', views.PostView.as_view(), name='postview'),
]