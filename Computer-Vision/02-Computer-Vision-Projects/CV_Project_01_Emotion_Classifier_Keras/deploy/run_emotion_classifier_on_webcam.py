#!/usr/bin/env python3

# Run Emotion Classifier on a video and save output with predictions for each frame

# Imports
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array

# Load your pre-trained model
model = tf.keras.models.load_model('ResNet50_Transfer_Learning_40_Epochs.keras')

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Initialize the face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def predict_emotions(video_path, output_path):
  """
  Analyzes a video, predicts emotions for each frame, and saves the output video with annotations.

  Args:
    video_path: The path to the video file.
    output_path: The path to save the output video with annotations.
  """
  # Start capturing video from the provided path
  cap = cv2.VideoCapture(video_path)

  # Get video properties for output video creation
  fps = cap.get(cv2.CAP_PROP_FPS)
  width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  # Define video writer for output
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Adjust codec if needed (e.g., 'XVID' for avi output)
  out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

  # Continuous loop for processing video frames
  while True:
    ret, frame = cap.read()
    if not ret:
      break

    # Detect faces in the grayscale frame
    faces = face_classifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    # Process each face detected
    for (x, y, w, h) in faces:
      # Draw a rectangle around each detected face
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
      # Extract the region of interest (ROI) i.e. the face area from the grayscale frame
      face = frame[y:y + h, x:x + w]
      # Resize the ROI to the size expected by the model (224x224 pixels in this case)
      face = cv2.resize(face, (224, 224))
      face = face.astype("float") / 255.0  # Normalize pixel values
      face = img_to_array(face)
      face = np.expand_dims(face, axis=0)  # Add batch dimension

      prediction = model.predict(face)[0]
      emotion = emotion_labels[np.argmax(prediction)]
      label_position = (x, y - 10)

      cv2.putText(frame, emotion, label_position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # Write the annotated frame to the output video
    out.write(frame)

    # Show the frame with the detected faces and emotion labels
    cv2.imshow("Emotion Classifier", frame)  # Comment this line in Jupyter Notebook

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Release resources
  cap.release()
  out.release()
  cv2.destroyAllWindows()

# Example usage (replace paths with your video and desired output)
video_path = 'path/to/your/video.mp4'  # video_path = 0 for Webcam video
output_path = 'path/to/save/output_video_with_emotions.mp4'  # Adjust extension based on codec
predict_emotions(video_path, output_path)