"""
ASGI config for Real_Time_Chat_App project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

# asgi.py: entry point for all incoming connections (HTTP + WebSocket)




import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application # Imports Django's built-in ASGI handler, which processes standard HTTP requests the traditional Django way.
from channels.auth import AuthMiddlewareStack # Imports middleware that populates the user session for WebSocket connections, so you can access scope["user"] in your consumers — similar to request.user in regular Django views.
from chat.routing import websocket_urlpatterns

# websocket_urlpatterns : Imports the WebSocket URL patterns defined in your chat app's routing.py — these map WebSocket URLs to their specific consumer classes.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Real_Time_Chat_App.settings')

'''os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Real_Time_Chat_App.settings')
Tells Django which settings file to use (Real_Time_Chat_App/settings.py). 
setdefault only sets it if it hasn't already been set, 
so it won't override an environment-level override.'''



# application = get_asgi_application()

# application = ProtocolTypeRouter({}) # main AsGI app
# ProtocolTypeRouter() : routes incoming connections based on their protocol type (HTTP vs WebSocket)
# URLRouter : routes WebSocket connections to the correct consumer based on URL patterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})

# "http": get_asgi_application() ------ All regular HTTP requests are handled by Django's standard request/response pipeline.

""""
websocket" → AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
WebSocket connections go through three layers (inside → out):

a. URLRouter — matches the WS URL to the right consumer
b. AuthMiddlewareStack — wraps it with auth/session support
c. ProtocolTypeRouter — the outermost router that directed it here"""

'''
HTTP requests  → urls.py (Django)
WebSocket      → routing.py (Channels)
'''