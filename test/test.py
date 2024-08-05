from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Qt
import sys
from modules.gui import gui


if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = gui.MainWindow()
    window.show()
    app.exec()








































# import logging
# import sys
# import cam
# import glob
# import cv2
# import os
# import object_tracker

# camera = cam.Cam()
# camera.setSource()
# camera.calibrate((7, 7), "./cam_sample", ".jpg", "r")
# f = 0
# while True:
#     cap = cv2.VideoCapture(camera.getSource())
#     (grabbed, img) = cap.read()
#     img = cam.pictureCut(img, 'r')
#     img = camera.unisort(img)
#     model_yolo = object_tracker.Object_Tracker()
#     model_yolo.setSource(img)
#     print(f)
#     result = model_yolo.track()
#     for r in result:
#         print(r.boxes.xywh)
#     f+=1