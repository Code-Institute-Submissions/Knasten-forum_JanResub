from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from django.http import HttpResponseRedirect
from .forms import AddPost, EditPost, CommentForm
from .models import Game, Post, Comment
from django.urls import reverse_lazy, reverse

# Create your views here.

def LikeView(request, id):
    print(request, id)
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('postview', args=[id]))

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


# class PostView(ListView):
#     model = Post
#     queryset = Post.objects.all()
#     template_name = 'postview.html'

class PostView(View):

    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)
        comments = post.comments.all()
        return render(
            request,
            "postview.html",
            {
                'post': post,
                'comments': comments,
            },
        )

class Add_Post(CreateView):
    model = Post
    form_class = AddPost
    template_name = 'add-post.html'
    def get_success_url(self):
        return reverse('postview', kwargs={'id': self.object.id})

class Add_Comment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add-comment.html'
    def get_success_url(self):
        return reverse('postview', kwargs={'id': self.object.id})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['id']
        return super().form_valid(form)

    success_url = reverse_lazy('home')



class Edit_Post(UpdateView):
    model = Post
    form_class = EditPost
    template_name = 'edit-post.html'