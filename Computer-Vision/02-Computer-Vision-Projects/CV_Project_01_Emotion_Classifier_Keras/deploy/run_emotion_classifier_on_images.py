#!/usr/bin/env python3

# Emotion Classifier Taipy App - Run Emotion Classifier on user uploaded images & get predictions

# Imports
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from taipy.gui import Gui, notify

# Load your pre-trained model
model = tf.keras.models.load_model('./ResNet50_Transfer_Learning_40_Epochs.keras')

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Initialize the face classifier
face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')


# Function to predict emotion
def predict_emotion(image):
    faces = face_classifier.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    emotions = []
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        face = cv2.resize(face, (224, 224))
        face = face.astype("float") / 255.0
        face = img_to_array(face)
        face = np.expand_dims(face, axis=0)

        prediction = model.predict(face)[0]
        emotion = emotion_labels[np.argmax(prediction)]
        emotions.append((x, y, w, h, emotion))
    return emotions


def analyze_image(state):
    if state.image_file:
        nparr = np.frombuffer(state.image_file, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        state.image = image
        state.emotions = predict_emotion(image)
        notify(state, 'image_source', 'render_image')


def render_image(state):
    if state.image is not None:
        image = state.image.copy()
        for (x, y, w, h, emotion) in state.emotions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        _, img_encoded = cv2.imencode('.jpg', image)
        return img_encoded.tobytes()
    return None


# Define GUI content
image_content = """
# Emotion Classifier

<|layout|columns=1 1|gap=10px|
<|
<|label|Image Upload|>
<|file|value=image_file|on_change=analyze_image|accept=image/*|label=Upload Image|>

|>
<|
<|image|source=image_source|width=600px|>
|>
|>

"""

# Initialize GUI
state = {
    'image_file': None,
    'image': None,
    'emotions': []
}

gui = Gui(page=image_content)
gui.run(state=state, title="Emotion Classifier App", host="0.0.0.0", port=5000, image_source=render_image)
