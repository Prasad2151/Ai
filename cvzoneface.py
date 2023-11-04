import cv2
from cvzone.FaceDetectionModule import FaceDetector
cap = cv2.VideoCapture(1)
detector = FaceDetector()
while True :
    success, img = cap.read()
    img, bBoxes = detector.findFaces(img)

    cv2.imshow("img",img)
    cv2.waitKey(1)

