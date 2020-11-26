import datetime

from django.contrib import messages
from django.db.models import F, Max
from django.http import HttpResponseRedirect
from django.shortcuts import render

from market.models import Market, Comment, Photo
from user.models import User
import json

def mylist(request, page=1):
    kwd = request.GET.get('kwd')

    if kwd is None or kwd == '' or kwd == 'null':
        start = (page - 1) * PAGESIZE
        market_count = Market.objects.count()
        marketlist = Market.objects.all().order_by('-groupno', 'orderno')[start:start + PAGESIZE]

    else:
        start = (page - 1) * PAGESIZE
        market_count = Market.objects.filter(title__contains=kwd).count()
        marketlist = Market.objects.filter(title__contains=kwd).order_by('-groupno', 'orderno')[start:start + PAGESIZE]

    data = {
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
    return render(request, 'market/mylist.html', data)


def mycomment(request):
    comments = Comment.objects.all()

    data = {
        'comments' : comments,
    }
    return render(request, 'market/mycomment.html', data)


def writeform(request, no=-1, page=1):
    # 인증
    authuser = request.session.get('authUser')
    if authuser is None:
        return HttpResponseRedirect('/market/list')

    if no == -1:
        return render(request, 'market/write.html', {"page": page})
    else:
        data = {"no": no, "page": page}
        # 검색어
        kwd = request.GET.get('kwd')
        if kwd is None:
            data['kwd'] = json.dumps(kwd)
        else:
            data['kwd'] = kwd
        return render(request, 'market/write.html', data)


def write(request, page=1):
    # 인증
    authuser = request.session.get('authUser')
    if authuser is None:
        return HttpResponseRedirect('/market/list')
    market = Market()
    market.title = request.POST['title']
    market.price = request.POST['price']
    market.content = request.POST['content']
    market.category = request.POST.get('category')
    market.user = User.objects.get(id=request.session['authUser']['id'])
        # return redirect('/detail/' + str(post.id))

    # 새글 작성
    if request.POST['no'] == '-1':
        value = Market.objects.aggregate(max_groupno=Max('groupno'))
        market.groupno = value["max_groupno"]+1
        market.save()

    # 답글 작성
    else:
        market2 = Market.objects.get(id=request.POST['no'])
        Market.objects.filter(orderno__gte=market2.orderno+1).update(orderno=F('orderno') + 1)
        market.groupno = market2.groupno
        market.orderno = market2.orderno+1
        market.depth = market2.depth + 1
        market.save()

    for img in request.FILES.getlist('imgs'):
        photo = Photo()
        photo.post = market
        photo.image = img
        photo.save()
    data = {
        'page': 1
    }
    # 검색어

    kwd = request.GET.get('kwd')
    print(kwd, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd
    return HttpResponseRedirect(f'/market/list/{page}?kwd={kwd}')


def view(request, no=0, page=1):
    # 존재하는 게시글이 없을 경우 return
    if no == 0:
        return HttpResponseRedirect('list')

    market = Market.objects.filter(id=no)
    comments = Comment.objects.filter(blog_id=no)

    data = {
        'market': market[0],
        'page': page,
        'comments': comments
    }
    authuser = request.session.get('authUser')
    if authuser is None:
        return render(request, 'market/view.html', data)
    comment = Comment()
    comment.blog = Market.objects.get(id=no)
    comment.comment_textfield = request.POST.get('comment_textfield')
    if comment.comment_textfield is None:
        return render(request, 'market/view.html', data)
    comment.comment_date = request.POST.get('comment_date')
    comment.comment_user = User.objects.get(id=request.session['authUser']['id'])
    comment.save()
    # 검색어
    kwd = request.GET.get('kwd')
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd

    response = render(request, 'market/view.html', data)
    # [1] 로그인 확인
    if request.session.get('authUser') is None:
        cookie_name = 'hit'
    else:
        cookie_name = f'hit:{request.session["authUser"]["id"]}'

    # [2] 그 날 당일 밤 12시에 쿠키 삭제
    tomorrow = datetime.datetime.replace(datetime.datetime.now(), hour=23, minute=59, second=0)
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")

    # [3] hit를 check하는 쿠키가 있는 경우
    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(no) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{no}', expires=expires)
            market.update(hit=F('hit') + 1)
            return response

    else:
        response.set_cookie(cookie_name, no, expires=expires)
        market.update(hit=F('hit') + 1)
        return response

    return render(request, 'market/view.html', data)


def modifyform(request, no=0, page=1):
    # 인증
    market = Market.objects.filter(id=no)[0]
    authuser = request.session.get('authUser')
    if authuser is None or market.user.id != authuser['id']:
        return HttpResponseRedirect('/market/list')

    data = {
        'market': market,
        'page': page,
    }

    # 검색어
    kwd = request.GET.get('kwd')
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd

    return render(request, 'market/modify.html', data)


def modify(request, page=1):
    market_id = request.POST['id']
    market = Market.objects.get(id=market_id)
    market.title = request.POST['title']
    market.price = request.POST['price']
    market.content = request.POST['content']
    market.category = request.POST.get('category')
    market.save()
    for img in request.FILES.getlist('imgs'):
        photo_id = request.POST['id']
        photo = Photo.objects.get(id=photo_id)
        photo.post = market
        photo.image = img
        photo.save()
    data = {
        'market': market,
        # page 추가
        'page': page,
    }

    # 검색어 추가
    kwd = request.GET.get('kwd')
    # 자바스크립트를 위한 처리
    if kwd is None:
        data['kwd'] = json.dumps(kwd)
    else:
        data['kwd'] = kwd

    return HttpResponseRedirect('/market/' + market_id + '/' + str(page), data)


def delete(request, no=0, page=1):
    market = Market.objects.get(id=no)
    authuser = request.session.get('authUser')
    if authuser is None or market.user.id != authuser['id']:
        return HttpResponseRedirect('/market/list')

    market.delete()
    return HttpResponseRedirect(f'/market/list/{page}')



PAGESIZE = 10
def list(request, page=1):
    kwd = request.GET.get('kwd')

    if kwd is None or kwd == '' or kwd == 'null':
        start = (page - 1) * PAGESIZE
        market_count = Market.objects.count()
        marketlist = Market.objects.all().order_by('-groupno', 'orderno')[start:start + PAGESIZE]

    else:
        start = (page - 1) * PAGESIZE
        market_count = Market.objects.filter(title__contains=kwd).count()
        marketlist = Market.objects.filter(title__contains=kwd).order_by('-groupno', 'orderno')[start:start + PAGESIZE]

    data = {
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

    return render(request, 'market/list.html', data)
