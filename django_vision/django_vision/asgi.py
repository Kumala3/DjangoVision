import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from detection_app.consumers import ObjectDetectionConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_vision.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/detect/", ObjectDetectionConsumer.as_asgi()),
                ]
            )
        ),
    }
)
