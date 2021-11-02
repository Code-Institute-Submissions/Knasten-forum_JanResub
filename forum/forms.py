from .models import Post, Game, Comment
from django import forms


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'game')


class EditPost(forms.ModelForm):
    pass


class CommentForm(forms.ModelForm):
    pass