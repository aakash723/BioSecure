import cv2
import numpy as np

# Load the pre-trained face recognition model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the known image and train the face recognizer
image_path = "C:\\Users\\KIIT0001\\Desktop\\my_projects\\sec_face_cam\\employees\\img22-03-24.jpg"
known_face = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# If face recognition should be based on the grayscale image, we need to set the label and ID
# For simplicity, we use a dummy ID of 1 for the "known" face

# Prepare a list for the training (image and ID)
faces = [known_face]
labels = [1]  # ID for the "known" face

# Create a face recognizer and train it with the data
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the current frame
    faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through the detected faces
    for (x, y, w, h) in faces_detected:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Get the face from the frame
        face = gray[y:y + h, x:x + w]

        # Recognize the face and get the label (ID) and confidence (the matching score)
        label, confidence = recognizer.predict(face)

        if confidence < 100:
            # If confidence is low, it means the match is accurate (lower confidence indicates a good match)
            cv2.putText(frame, f'Known', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            # If confidence is high, it means it doesn't match
            cv2.putText(frame, f'Unknown', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
