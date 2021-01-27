import cv2 as cv
import numpy as np


image = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png")
h, w = image.shape[:2]
src = np.array([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]], np.float32)
dst = np.array([[80, 80], [w/2, 50], [80, h-80], [w-40, h-40]], np.float32)
M = cv.getPerspectiveTransform(src, dst)
image1 = cv.warpPerspective(image, M, (w, h), borderValue=125)
# 显示图像
cv.imshow("image", image)
cv.imshow("image1", image1)
cv.waitKey()
cv.destroyAllWindows()