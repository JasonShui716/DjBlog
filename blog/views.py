from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .trade.HuobiServices import *
import json


# Create your views here.

def index(request):
    # return HttpResponse("Welcome to my blog")
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request):
    return HttpResponse("1")


@csrf_exempt
def btc_trade(request):
    if request.method == 'GET':
        ticker = get_ticker('btcusdt')
        btc_curr = ticker['tick']['close']
        # btc_curr = 3433.33
        return HttpResponse(json.dumps({"btc": btc_curr}))
