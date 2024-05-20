from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("card", views.showCard, name="showCard"),
    path("database", views.showAllCards, name="cardDatabase"),
    path("deck", views.showDeck, name="deck"),
    path("expansiones", views.expansiones, name="expansiones"),
    path("expansion", views.showExpantion, name="showExpantion"),
]