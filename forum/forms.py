from .models import Post, Game, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget

games = Game.objects.all().values_list('name', flat=True)
game_list = [game for game in games]


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'game', 'author')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'content': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your post content here!',
            }),
            'game': forms.Select(choices=game_list, attrs={
                'class': 'form-control mb-3',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'author-id',
                'type': 'hidden',

            })
          
        }


class EditPost(forms.ModelForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content', 'post')

        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'author-id',
                'type': 'hidden',

            }),
            'content': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment here!',
            }),
            'post': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'post-id',
                'type': 'hidden',
            })
        }
