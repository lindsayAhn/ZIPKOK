from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    authuser = request.session.get('authUser')
    if authuser is None:
        return HttpResponseRedirect('/')
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })