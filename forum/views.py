from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import AddPost, CommentForm
from .models import Game, Post, Comment
from django.urls import reverse_lazy, reverse


def LikeView(request, id):
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
                'posts': posts,
            },
        )


class PostView(View):

    def get(self, request, id, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)
        comments = post.comments.all()
        total_likes = post.likes.count()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        return render(
            request,
            "postview.html",
            {
                'post': post,
                'comments': comments,
                'liked': liked,
            },
        )


class Add_Post(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPost
    template_name = 'add-post.html'

    def get_success_url(self):
        return reverse('postview', kwargs={'id': self.object.id})


class Add_Comment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add-comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postview', kwargs={'id': self.object.post_id})


class Delete_Post(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    def get_success_url(self):
        return reverse('postlist', kwargs={'name': self.object.game})


class Delete_Comment(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'
    def get_success_url(self):
        return reverse('postview', kwargs={'id': self.object.post_id})