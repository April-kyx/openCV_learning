import cv2 as cv


image1 = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png")
cv.imshow("image1", image1)
image2 = cv.cvtColor(image1, cv.COLOR_BGR2RGB)
image3 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
cv.imshow("image2", image2)
cv.imshow("image3", image3)
image4 = cv.cvtColor(image1, cv.COLOR_BGR2YCrCb)
cv.imshow("image4", image4)
image5 = cv.cvtColor(image1, cv.COLOR_BGR2HSV)
cv.imshow("image5", image5)
cv.waitKey()
cv.destroyAllWindows()