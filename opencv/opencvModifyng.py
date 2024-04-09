import numpy as np
import cv2 as cv

img = cv.imread('E:\\Captures\\ELDEN_RING_2023_1_14 14_09_12.png')

assert img is not None, "file could not be read, check with os.path.exists()"

# 获取像素点
px = img[100, 100]

print(px)

# 仅返回蓝色通道
# 蓝：0，绿：1，红：2

blue = img[100, 100, 0]

print(blue)

print(img.size)

print(img.dtype)