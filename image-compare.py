import cv2
import numpy as np

image1 = cv2.imread("korea_03.png")
image2 = cv2.imread("korea_04.png")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)

if result is True:
    print("The images are the same")

else:
    cv2.imwrite("difference.jpg", difference)
    print("The images are different")