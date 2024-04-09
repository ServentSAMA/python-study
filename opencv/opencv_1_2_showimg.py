import cv2 as cv

img = cv.imread('E:\\Captures\\ELDEN_RING_2023_1_14 14_09_12.png')

cv.namedWindow('image', cv.WINDOW_FULLSCREEN)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyWindows('image')