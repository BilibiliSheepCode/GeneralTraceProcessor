import logging
import sys
import modules.cam.cam as cam
import glob
import cv2
import os
import numpy as np
import modules.object_tracker.object_tracker as object_tracker

stereo = cam.Cam(True, './Camera')
# stereo.param['resolution']=(3840,1080)
# stereo.capture()
# stereo.calibrate((7, 7), './Samples', '.jpg', 'a')
# img=cv2.imread('./Samples/0.jpg')
# imgl,imgr=stereo.rectify(img)
# cv2.imwrite('l.jpg',imgl)
# cv2.imwrite('r.jpg',imgr)

# stereo.setSource(1)
# # stereo.setStoreDir('./Samples')
# cap = cv2.VideoCapture(camerar.getSource())
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, camerar.param['resolution'][0])
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camerar.param['resolution'][1])
# (grabbed, img) = cap.read()
# sl,sr=s.rectifyImage(img)
# cv2.imwrite('l.jpg',sl)
# cv2.imwrite('r.jpg',sr)
# cameral.calibrate((7, 7), './Samples0', '.jpg', 'l')
# camerar.calibrate((7, 7), './Samples0', '.jpg', 'r')
f = 0
while True:
    cap = cv2.VideoCapture(stereo.getSource())
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, stereo.param['resolution'][0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, stereo.param['resolution'][1])
    (grabbed, img) = cap.read()
    while not grabbed or not cap.isOpened():
        (grabbed, img) = cap.read()
    imgl,imgr = stereo.rectify(img)
    model_yolo = object_tracker.Object_Tracker()
    model_yolo.setSource(imgl)
    resultl = model_yolo.track()
    model_yolo.setSource(imgr)
    resultr = model_yolo.track()
    print(f)
    print('l')
    for r in resultl:
        print(r.boxes.xywh)
    print('r')
    for r in resultr:
        print(r.boxes.xywh)
    f+=1

# 创建 SGBM 视差计算对象
blockSize = 16
img_channels = 3
stereo = cv2.StereoSGBM_create(
    minDisparity=1,
    numDisparities=64,
    blockSize=blockSize,
    P1=8 * img_channels * blockSize * blockSize,
    P2=32 * img_channels * blockSize * blockSize,
    disp12MaxDiff=-1,
    preFilterCap=1,
    uniquenessRatio=10,
    speckleWindowSize=100,
    speckleRange=100,
    mode=cv2.STEREO_SGBM_MODE_HH
)
disparity = stereo.compute(imgl, imgr)

disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
dis_color = disparity
dis_color = cv2.normalize(dis_color, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
dis_color = cv2.applyColorMap(dis_color, 2)
cv2.imwrite("depth.png", dis_color)
cv2.imwrite('gray.png', disp)
# # 计算视差图
# disparity = stereo.compute(imgl, imgr)

# # 可视化视差图
# cv2.imshow('Disparity Map', disparity)
# cv2.imwrite('./Result.jpg',disparity)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





















# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
# from PySide6.QtCore import Qt
# import sys
# from modules.gui import gui


# if __name__ == '__main__':
#     app = QApplication.instance()
#     if app is None:
#         app = QApplication(sys.argv)
#     window = gui.MainWindow()
#     window.show()
#     app.exec()