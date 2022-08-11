from django.urls import path

from myapp.consumers import AuthorBookWebsocketConsumer

urlpatterns = [
    path('wss/test/', AuthorBookWebsocketConsumer.as_asgi())
]
