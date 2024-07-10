from django.urls import path
from detection_app.consumers import ObjectDetectionConsumer

websocket_urlpatterns = [
    path("ws/detect/", ObjectDetectionConsumer.as_asgi()),
]
