import cv2 as cv
import numpy as np


image = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png")
print(image.shape[:2])
h, w = image.shape[:2]
# 缩放
M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
imageMove = cv.warpAffine(image, M, (w, h))
cv.imshow("image", image)
cv.imshow("imageMove", imageMove)
# 旋转
M1 = cv.getRotationMatrix2D((w/3, h/3), -40, 0.4)
imageRota = cv.warpAffine(image, M1, (w, h))
cv.imshow("imageRota", imageRota)
cv.waitKey()
cv.destroyAllWindows()