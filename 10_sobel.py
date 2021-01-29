import cv2 as cv


image = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png", 0)
sobelx = cv.Sobel(image, cv.CV_64F, 1, 0)
sobelx = cv.convertScaleAbs(sobelx)
sobely = cv.Sobel(image, cv.CV_64F, 0, 1)
sobely = cv.convertScaleAbs(sobely)
sobelxy = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv.imshow("image", image)
cv.imshow("sobelxy", sobelxy)
cv.waitKey()
cv.destroyAllWindows()