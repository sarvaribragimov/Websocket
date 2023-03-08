from django.urls import path
from .views import index_view,roomview

urlpatterns = [
    path('',index_view,name='chat_index'),
    path('<str:room_name>/',roomview,name='chat_room')
]
