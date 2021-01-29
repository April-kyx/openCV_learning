import cv2 as cv


image = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png", 0)
img0 = image
img1 = cv.pyrDown(img0)
img2 = cv.pyrDown(img1)
img3 = cv.pyrDown(img2)
I0 = img0 - cv.pyrUp(img1)
I1 = img1 - cv.pyrUp(img2)
I2 = img2 - cv.pyrUp(img3)
cv.imshow("I0", I0)
cv.imshow("I1", I1)
cv.imshow("I2", I2)
cv.waitKey()
cv.destroyAllWindows()