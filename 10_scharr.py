import cv2 as cv


image = cv.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png", 0)
scharrx = cv.Scharr(image, cv.CV_64F, 1, 0)
scharrx = cv.convertScaleAbs(scharrx)
scharry = cv.Sobel(image, cv.CV_64F, 0, 1)
scharry = cv.convertScaleAbs(scharry)
scharrxy = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
cv.imshow("image", image)
cv.imshow("scharrxy", scharrxy)
cv.waitKey()
cv.destroyAllWindows()