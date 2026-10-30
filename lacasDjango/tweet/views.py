from django.shortcuts import render, redirect

from .models import Tweet
from .forms import TweetForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, "index.html")


def tweet_list(request):
    all_tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "tweet_list.html", {'tweets': all_tweets})

@login_required
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

@login_required
def edit_tweet(request , tweet_id):
    tweet = Tweet.objects.get(id=tweet_id , user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)

        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request , "tweet_form.html" , {'form' : form})

@login_required
def delete_tweet(request , tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.delete()
    return redirect('tweet_list')


def personal(request):
    user = request.user
    return render(request , "personal.html" , {'user' : user})




def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("tweet_list")
    else:
        form = UserCreationForm()
    return render(request , "register.html" , {'form' : form})