import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[ERROR] Camera not accessible.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to grab frame.")
        break

    cv2.imshow("Test Camera", frame)

    # Press 'q' to quit the camera feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
