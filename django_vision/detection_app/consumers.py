import json
import cv2
import numpy as np
import tensorflow as tf
from channels.generic.websocket import AsyncWebsocketConsumer
from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input,
    decode_predictions,
)
from tensorflow.keras.applications import MobileNetV2


class ObjectDetectionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.model = MobileNetV2(weights="imagenet")

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        frame = text_data_json["frame"]

        # Convert base64 image to numpy array
        nparr = np.frombuffer(frame.encode(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Preprocess the image
        img = cv2.resize(img, (224, 224))
        img = preprocess_input(img)
        img = np.expand_dims(img, axis=0)

        # Perform object detection
        predictions = self.model(img, training=False)
        decoded_predictions = decode_predictions(predictions.numpy(), top=1)[0]

        # Get the top prediction
        top_prediction = decoded_predictions[0]
        object_name, confidence = top_prediction[1], float(top_prediction[2])

        # Send the result back to the client
        await self.send(
            text_data=json.dumps({"object": object_name, "confidence": confidence})
        )
