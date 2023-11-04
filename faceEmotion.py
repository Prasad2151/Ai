import cv2
import numpy as np
from keras.models import load_model

# Load your pre-trained model
model = load_model('emotion_model.hdf5')

# Define emotion labels
emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

# Create a function to perform emotion detection on each frame
def detect_emotion(frame):
    # Preprocess the image
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_resized = cv2.resize(frame_gray, (64, 64))
    frame_normalized = frame_resized / 255.0
    frame_input = frame_normalized.reshape(1, 64, 64, 1)

    # Make predictions
    emotions = model.predict(frame_input)
    predicted_emotion = emotion_labels[emotions.argmax()]

    return predicted_emotion

# Open a connection to the camera (0 is usually the default camera)
cap = cv2.VideoCapture(1)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Perform emotion detection on the frame
    detected_emotion = detect_emotion(frame)

    # Display the detected emotion at the bottom left of the frame
    cv2.putText(frame, "Emotion: " + detected_emotion, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)

    # Show the frame with the detected emotion
    cv2.imshow('Emotion Detection', frame)

    # Print the detected emotion to the console
    print("Detected Emotion:", detected_emotion)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()

