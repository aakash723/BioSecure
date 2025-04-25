# BioSecure

---

# **Project Portfolio: FaceGuard - Real-Time Face Recognition Security System**

## **Project Overview**
**FaceGuard** is a real-time face recognition security system developed using Python, OpenCV, Dlib, and TensorFlow. The system provides efficient access control by verifying individuals based on facial features, ensuring secure entry into restricted areas.

## **Key Features**
- **Real-Time Face Detection & Recognition:** Utilizes OpenCV's Haar Cascade Classifier for face detection and TensorFlow's neural networks for face recognition.
- **Access Control:** Displays a green signal ("Access Granted") for recognized faces and a red signal ("Unknown") for unrecognized ones.
- **User-Friendly Interface:** Clear visual feedback for authorized/unauthorized users.
- **Database Management:** Stores labeled face images for comparison, allowing easy addition of new users.

## **Functionality**
- **Face Detection:** Captures faces via webcam and processes them in real time using Haar Cascade.
- **Neural Network Integration:** Matches detected faces against the stored database using a neural network model, with facial features encoded and compared for recognition.
- **Security Response:** Grants or denies access based on facial recognition accuracy, with visual signals indicating success or failure.

## **Challenges**
- **Image Quality Variability:** Improved model accuracy through diverse, high-resolution training data.
- **Lighting & Angle Differences:** Enhanced robustness by augmenting the dataset for varied conditions.

## **Future Enhancements**
- **Cloud Database Integration** for distributed access.
- **Multi-Factor Authentication** for added security.

**Technologies:** Python, OpenCV, TensorFlow, Dlib  
**Hardware:** Webcam

---
