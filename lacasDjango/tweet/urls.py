from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),
    path("create_tweet/", views.create_tweet, name="create_tweet"),
    path("edit_tweet/<int:tweet_id>/", views.edit_tweet, name="edit_tweet"),
    path("delete_tweet/<int:tweet_id>/", views.delete_tweet, name="delete_tweet"),

    path("personal/", views.personal, name="personal"),

    path("accounts/login/", views.user_register, name="register"),
]