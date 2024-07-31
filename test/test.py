import logging
import sys
import cam
import glob
import cv2
import os
import object_tracker

camera = cam.Cam()
camera.setSource()
model_yolo = object_tracker.Object_Tracker()
model_yolo.setSource(camera.getSource())
model_yolo.track()
# camera.calibrate((7, 7), "./cam_sample", ".jpg", "r")
# images = glob.glob("./cam_sample/*.jpg")
# cv2.namedWindow('Result', cv2.WINDOW_KEEPRATIO)
# cv2.resizeWindow('Result', 800, 600)
# cv2.imshow('Result', camera.unisort(cam.pictureCut(cv2.imread(images[0]),'r')))
# cv2.waitKey(10000)