import cv2
import numpy as np


cap = cv2.VideoCapture("E:\\阿凡达：水之道.Avatar.The.Way.of.Water.2022.1080p.BluRay.x264.DTS-CNXP.mkv")
fps = cap.get(cv2.CAP_PROP_FPS)
while (True):
    # 读帧
    ret, frame = cap.read()
    # 显示图像
    cv2.imshow("video", frame)
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break
# 释放cap
cap.release()
# 关闭窗口，清除程序所占用的内存
cv2.destroyAllWindows()


