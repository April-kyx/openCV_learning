import cv2 as cv
import matplotlib.pyplot as plt


image = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png")
# hist = cv.calcHist([image], [1], None, [256], [0, 256])
# plt.plot(hist)
# plt.show()
image = image.ravel()
plt.hist(image, 256)
cv.waitKey()
cv.destroyAllWindows()
plt.show()
