# Python code to read image
import cv2

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("dog.jpg", cv2.IMREAD_COLOR)
#line = cv2.line(img, (0, 0), (400, 400), (0,0,255), 2)
#circle = cv2.circle(img, (500,500), 200, (0,0,255), 2)
#rect = cv2.rectangle(img, (200,200), (700,700), (255,0,0), 2)

cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
