#!/usr/bin/env python3

# EmotionScope Gradio App - Run Emotion Classifier on user uploaded images & get predictions

# Imports
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from huggingface_hub import hf_hub_download
import gradio as gr

# Download the best ResNet50 model if not already present
if not os.path.exists("ResNet50_Transfer_Learning_40_Epochs.keras"):
    hf_hub_download(
        repo_id="ancilcleetus/EmotionScope",
        filename="ResNet50_Transfer_Learning_40_Epochs.keras",
        local_dir=".",
    )

model_path = "ResNet50_Transfer_Learning_40_Epochs.keras"

# Load the pretrained model
model = load_model(model_path)

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Initialize the face classifier
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# Function to predict emotion
def predict_emotion(image):
    # Convert PIL image to OpenCV format (BGR)
    opencv_image = np.array(image)[:, :, ::-1].copy()  # Convert RGB to BGR

    faces = face_classifier.detectMultiScale(opencv_image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)

    # Check for detected faces
    if len(faces) == 0:
        return "No faces detected"

    # Process the first face
    (x, y, w, h) = faces[0]
    face = opencv_image[y:y + h, x:x + w]
    face = cv2.resize(face, (224, 224))
    face = face.astype("float") / 255.0
    face = img_to_array(face)
    face = np.expand_dims(face, axis=0)

    prediction = model.predict(face)[0]
    emotion = emotion_labels[np.argmax(prediction)]

    return emotion


# Define the Gradio interface
gif_url = "https://i.postimg.cc/P5wNJRDN/CV-Project-01-Emotion-Scope-01.gif"  # Direct link to your GIF

interface = gr.Interface(
    fn=predict_emotion,  # Your prediction function
    inputs=gr.Image(type="pil"),  # Input for uploading an image, directly compatible with PIL images
    outputs="text",  # Output as text displaying the predicted emotion
    title="EmotionScope",
    description=f"""
    <b><span style='font-size: 20px;'>Upload Your Photo, Unveil Your Emotion!</span></b><br>
    <img src="{gif_url}" alt="Animation" width="300" height="300">
    """
)

# Launch the Gradio interface
interface.launch(share=True)
