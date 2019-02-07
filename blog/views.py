from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post
from .trade.HuobiServices import *
from .Util import *
import requests
import json
import time


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

@csrf_exempt
def csdn_feed(request):
    if request.method == 'GET':
        t = str(time.time()*1000000)
        res = requests.get("https://www.csdn.net/api/articles?type=more&category=home&shown_offset="+t)
        pretty_json = deal_json_invaild(res.text.encode('utf-8').decode('unicode-escape'))

        # TODO: solve the problem of invalid JSON
