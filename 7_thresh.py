import cv2 as cv


image = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png", 0)
ret, dst = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
cv.imshow("image", image)
cv.imshow("dst", dst)
admean = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 3)
adguass = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 3) # 这里输入图像一定是8位单通道
cv.imshow("admean", admean)
cv.imshow("adguass", adguass)
# Otsu阈值处理，选择最佳阈值
t2, otsu = cv.threshold(image, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("otsu", otsu)
print("二值化阈值处理的阈值是：%s" % ret)
print("Ostu阈值处理的阈值是：%s" % t2)
cv.waitKey()
cv.destroyAllWindows()