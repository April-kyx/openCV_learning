import cv2


image = cv2.imread(r"F:\PycharmProjects\pythonProject\openCV_learning\lena.png")
b, g, r = cv2.split(image)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()