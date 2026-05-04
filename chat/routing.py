from django.urls import path
from .consumers import ChatConsumer

'''
    What is routing.py ?
--> It connects WebSocket URL → Consumer (chat logic)
'''

websocket_urlpatterns = [
    path("ws/chat/<int:room_id>/", ChatConsumer.as_asgi()), # ChatConsumer.as_asgi() : This converts the class(ChatConsumer) into an ASGI-compatible app
]

# Need to converts ChatConsumer class into an ASGI-compatible app
# Django Channels expects ASGI callable
# Not plain Python class

# asgi.py → entry point
# routing.py → URL mapping
# consumers.py → logic

'''
HTTP requests  → urls.py (Django)
WebSocket      → routing.py (Channels)
'''