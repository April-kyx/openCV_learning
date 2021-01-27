import cv2 as cv
import numpy as np


# 构建一个6*6的随机数组
image = np.random.randint(0, 256, size=[6, 6], dtype=np.uint8)
w, h = image.shape
# 建立数组的大小
x = np.zeros((w, h), np.float32)
y = np.zeros((w, h), np.float32)
# 师兄新数组的访问操作
for i in range(w):
    for j in range(h):
        x.itemset((i, j), j)
        y.itemset((i, j), i)
print(x)
print(y)
rst = cv.remap(image, x, y, cv.INTER_LINEAR)
# 打印
print("image=\n", image)
print("rst=\n", rst)
