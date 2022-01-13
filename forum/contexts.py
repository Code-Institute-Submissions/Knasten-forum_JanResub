from .models import Game

def game_list(request):
    games = Game.objects.all()
    context = {
        'game_list': games,
    }
    return context