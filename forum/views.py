from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse
from .models import Game, Post, Comment

# Create your views here.

class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.all()
    template_name = 'index.html'


class PostList(View):

    def get(self, request, name, *args, **kwargs):
        queryset = Game.objects.all()
        game = get_object_or_404(queryset, name=name)
        posts = game.forum_posts.all()
        return render(
            request,
            "post.html",
            {
                'game': game,
                'posts': posts,
            },
        )


class PostView(generic.DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'postview.html'