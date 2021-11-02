from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from django.http import HttpResponse
from .forms import AddPost, EditPost, CommentForm
from .models import Game, Post, Comment

# Create your views here.

class GameList(ListView):
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
            "postlist.html",
            {
                'game': game,
                'posts': posts,
            },
        )


class PostView(DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'postview.html'


class Add_Post(CreateView):
    model = Post
    form_class = AddPost
    template_name = 'add-post.html'


class Edit_Post(UpdateView):
    model = Post
    form_class = EditPost
    template_name = 'edit-post.html'