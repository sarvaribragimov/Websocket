from django.shortcuts import render
from .models import Room
# Create your views here.

def index_view(request):
    return render(request,'index.html', {
        "rooms":Room.objects.all(),
    })

def roomview(request,room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request,'room.html', {
        'room':chat_room,
    })