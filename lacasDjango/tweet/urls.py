from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),
    path("create_tweet/", views.create_tweet, name="create_tweet"),
]
