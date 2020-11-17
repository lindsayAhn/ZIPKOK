from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from social.models import Recommendation
from user.models import User

def around(request):
    return render(request, 'social/around.html', {})


def art(request):
    return render(request, 'social/art.html', {})


def craft(request):
    return render(request, 'social/craft.html', {})


def workout(request):
    return render(request, 'social/workout.html', {})


def musicdance(request):
    return render(request, 'social/musicdance.html', {})


def instrument(request):
    return render(request, 'social/instrument.html', {})


def cook(request):
    return render(request, 'social/cook.html', {})


def homecafe(request):
    return render(request, 'social/homecafe.html', {})


def movies(request):
    return render(request, 'social/movies.html', {})


def books(request):
    return render(request, 'social/books.html', {})


def etc(request):
    return render(request, 'social/etc.html', {})

def accountform(request):
    return render(request, 'social/accountform.html', {})

def recommendation(request):

    authuser = request.session.get('authUser')
    if authuser is None:
        return HttpResponseRedirect('/')
    recommendation = Recommendation()
    recommendation.questType = request.POST['questType']
    recommendation.lowaccount = request.POST['lowaccount']
    recommendation.urladress = request.POST['urladress']
    recommendation.recommendationReason = request.POST['recommendationReason']

    recommendation.user = User.objects.get(id=request.session['authUser']['id'])

    recommendation.save()

    return HttpResponseRedirect('/')