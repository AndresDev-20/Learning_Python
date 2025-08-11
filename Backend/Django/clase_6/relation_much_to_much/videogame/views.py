from django.shortcuts import render
from .models import Game, User
from django.http import HttpResponse

# Create your views here.
def create_game(request):
    user1 = User(username="User1", email="user1@example.com", password="password1")
    user1.save()
    user2 = User(username="User2", email="user2@example.com", password="password2")
    user2.save()
    user3 = User(username="User3", email="user3@example.com", password="password3")
    user3.save()

    videogame1 = Game(title="Game 1", genre="Action", release_date="2023-01-01")
    videogame1.save()
    videogame2 = Game(title="Game 2", genre="Adventure", release_date="2023-02-01")
    videogame2.save()
    videogame3 = Game(title="Game 3", genre="RPG", release_date="2023-03-01")
    videogame3.save()

    videogame1.users.add(user1)
    videogame1.users.add(user2)
    videogame2.users.add(user2)
    videogame2.users.add(user3)
    videogame3.users.add(user1)
    videogame3.users.add(user3)

    return HttpResponse("Games and Users created with relationships.")