from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("games", views.games_view, name= "games"),
    path("games/rocket_boost", views.rocket_boost_view, name= "rocket_boost"),
    path("bot/rasa", views.rasa_bot_view, name="rasa-bot"),
]
