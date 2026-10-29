from django.shortcuts import render, redirect

from .models import Tweet
from .forms import TweetForm
# Create your views here.


def index(request):
    return render(request, "index.html")


def tweet_list(request):
    all_tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "tweet_list.html", {'tweets': all_tweets})


def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, "tweet_form.html", {'form': form})


def edit_tweet(request , tweet_id):
    tweet = Tweet.objects.get(id=tweet_id , user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)

        if form.is_valid():
            form.save()
            return redirect('tweet_list')
        
    else:
        form = TweetForm()
    return render(request , "tweet_form.html" , {'form' : form})


def delete_tweet(request , tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request , "confirm_delete_tweet.html" , {'tweet' : tweet})


def single_tweet(request , tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request , "single_tweet.html" , {'tweet' : tweet})


