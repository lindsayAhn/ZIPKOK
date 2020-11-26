from django.shortcuts import render
from board.models import Board
import json

# Create your views here.
from market.models import Market

PAGESIZE = 3
def index(request, page=1):
    kwd = request.GET.get('kwd')

    if kwd is None or kwd == '' or kwd == 'null':
        start = (page - 1) * PAGESIZE
        board_count = Board.objects.count()
        boardlist = Board.objects.all().order_by('-groupno', 'orderno')[start:start + PAGESIZE]
        market_count = Market.objects.count()
        marketlist = Market.objects.all().order_by('-groupno', 'orderno')[start:start + PAGESIZE]

    else:
        start = (page - 1) * PAGESIZE
        board_count = Board.objects.filter(title__contains=kwd).count()
        boardlist = Board.objects.filter(title__contains=kwd).order_by('-groupno', 'orderno')[start:start + PAGESIZE]
        market_count = Market.objects.filter(title__contains=kwd).count()
        marketlist = Market.objects.filter(title__contains=kwd).order_by('-groupno', 'orderno')[start:start + PAGESIZE]

    data = {
        'boardlist': boardlist,
        'board_count': board_count,
        'marketlist': marketlist,
        'market_count': market_count,
        'current_page': page,
        'page': page,
    }

    kwd = request.GET.get('kwd')
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd
    return render(request, 'main/index.html', data)


