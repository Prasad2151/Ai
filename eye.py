import cv2

# Load the Haar Cascade classifier for eye detection
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Initialize the webcam
cap = cv2.VideoCapture(1)  # 0 is typically the default camera

# Define variables to keep track of consecutive frames with closed eyes
closed_eyes_count = 0
drowsiness_threshold = 15  # Adjust as needed


while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the frame
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    if len(eyes) == 0:
        # Eyes not detected
        print("Eyes Not Detected")
        cv2.putText(frame, "Eyes Not Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    for (ex, ey, ew, eh) in eyes:
        # Draw rectangles around the detected eyes
        cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Calculate the midpoint of the eyes
        eye_midpoint = (ex + ew // 2, ey + eh // 2)
        print(eh)

        # Check if the eye region is relatively small, indicating possible eye closure
        if eh < 90:
            closed_eyes_count += 1
            cv2.putText(frame, "Drowsiness Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print("Drowsiness Detected")
        else:
            closed_eyes_count = 0


        if closed_eyes_count >= drowsiness_threshold:
            # Drowsiness detected, add an alert system here
            # For simplicity, let's display a text alert
            cv2.putText(frame, "Drowsiness Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            # Add an alert system here, such as playing a sound or displaying a visual warning

    cv2.imshow("Drowsiness Detection", frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

