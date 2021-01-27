import cv2 as cv
import numpy as np


image1 = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png")
cv.imshow("image", image1)
image2 = np.zeros(image1.shape, dtype=np.uint8)
image2[100:400, 100:400] = 255
image3 = cv.bitwise_and(image1, image2)
cv.imshow("image3", image3)
cv.waitKey()
cv.destroyAllWindows()