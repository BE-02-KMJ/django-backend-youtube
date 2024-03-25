# channels Library를 활용해서 Socket 연결하는 비동기 server(route) 구현 
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routes import websocket_urlpatterns
from djnago.core.asgi import get_asgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application,
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)    # ws://127.0.0.1:8000/ws/room
    )
})