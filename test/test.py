import logging
import sys
import modules.cam.cam as cam
import glob
import cv2
import os
import numpy as np
import math
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
# f = 0
# while True:
#     cap = cv2.VideoCapture(stereo.getSource())
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, stereo.param['resolution'][0])
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, stereo.param['resolution'][1])
#     (grabbed, img) = cap.read()
#     while not grabbed or not cap.isOpened():
#         (grabbed, img) = cap.read()
#     imgl,imgr = stereo.rectify(img)
#     model_yolo = object_tracker.Object_Tracker()
#     model_yolo.setSource(imgl)
#     resultl = model_yolo.track()
#     model_yolo.setSource(imgr)
#     resultr = model_yolo.track()
#     print(f)
#     print('l')
#     for r in resultl:
#         print(r.boxes.xywh)
#         print(stereo.getCoordinate(img, int(r.boxes.xywh[0][1]), int(r.boxes.xywh[0][1])))
#     print('r')
#     for r in resultr:
#         print(r.boxes.xywh)
#         print(stereo.getCoordinate(img, int(r.boxes.xywh[0][1]), int(r.boxes.xywh[0][1])))
#     f+=1

# 创建 SGBM 视差计算对象
blockSize = 16
img_channels = 3
sgbm = cv2.StereoSGBM_create(
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
sgbm = cv2.StereoSGBM_create(
            minDisparity=1,
            numDisparities=128,
            blockSize=blockSize,
            P1=8 * img_channels * blockSize * blockSize,
            P2=32 * img_channels * blockSize * blockSize,
            disp12MaxDiff=-1,
            preFilterCap=63,
            uniquenessRatio=15,
            speckleWindowSize=100,
            speckleRange=1,
            mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY #cv2.STEREO_SGBM_MODE_HH
        )
disparity = sgbm.compute(imgl, imgr)

disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
dis_color = disparity
dis_color = cv2.normalize(dis_color, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
dis_color = cv2.applyColorMap(dis_color, 2)
cv2.imwrite("depth.png", dis_color)
cv2.imwrite('gray.png', disp)
# threeD = cv2.reprojectImageTo3D(disparity, stereo.param['Q'], handleMissingValues=True)
# threeD = threeD * 16
# while True:
#     cv2.namedWindow('depth', cv2.WINDOW_KEEPRATIO)
#     cv2.resizeWindow('depth', 800, 600)
#     cv2.imshow("depth", dis_color)
#     def onmouse_pick_points(event, x, y, flags, param):
#         if event == cv2.EVENT_LBUTTONDOWN:
#             threeD = param
#             print('\n像素坐标 x = %d, y = %d' % (x, y))
#             # print("世界坐标是：", threeD[y][x][0], threeD[y][x][1], threeD[y][x][2], "mm")
#             print("世界坐标xyz 是：", threeD[y][x][0] / 1000.0, threeD[y][x][1] / 1000.0, threeD[y][x][2] / 1000.0, "m")

#             distance = math.sqrt(threeD[y][x][0] ** 2 + threeD[y][x][1] ** 2 + threeD[y][x][2] ** 2)
#             distance = distance / 1000.0  # mm -> m
#             print("距离是：", distance, "m")
#     cv2.setMouseCallback("depth", onmouse_pick_points, threeD)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
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