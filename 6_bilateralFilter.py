import cv2 as cv


image = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png")
cv.imshow("image", image)
gauss = cv.GaussianBlur(image, (55, 55), 0, 0)
bilateral = cv.bilateralFilter(image, 55, 100, 100)
cv.imshow("gauss", gauss)
cv.imshow("bilateral", bilateral)
cv.waitKey()
cv.destroyAllWindows()