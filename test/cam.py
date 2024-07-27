import cv2
import glob
import os
import numpy as np
import logging

def pictureCut(img, type):
    h,w = img.shape[:2]
    match type:
        case 'r':
            return img[0:h, w//2:w]
        case 'l':
            return img[0:h, 0:w//2]
        case 'a':
            return img

class Cam:
    def __init__(self) -> None:
        self.intrinsic_matrix = []
        self.distortion_cofficients = ()
        self.source = 0
        self.store_dir = "./pics"
        if not os.path.exists(self.store_dir):
            os.mkdir(self.store_dir)

    def capture(self):
        camera = cv2.VideoCapture(self.source)
        i = 0
        if not camera.isOpened():
            return False
        cv2.namedWindow('capture', cv2.WINDOW_KEEPRATIO)
        cv2.resizeWindow('capture', 800, 600)
        while True:
            (grabbed, img) = camera.read()
            cv2.imshow('capture', img)
            if cv2.waitKey(1) & 0xff == ord('c'):
                filename = str(self.store_dir + '/' + str(i) + '.jpg')
                if not cv2.imwrite(filename, img):
                    print("Error To Store " + filename)
                    i -= 1
                i += 1
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        cv2.destroyWindow("capture")
        return True

    def setSource(self):
        camera = cv2.VideoCapture(self.source)
        r = 0
        if not camera.isOpened():
            return False
        else:
            cv2.namedWindow('sources', cv2.WINDOW_KEEPRATIO)
            cv2.resizeWindow('sources', 800, 600)
            while True:
                if cv2.waitKey(1) & 0xff == ord('f'):
                    self.source = r
                    break
                elif cv2.waitKey(1) & 0xff == ord('n'):
                    r += 1
                    camera.release()
                    camera = cv2.VideoCapture(r)
                elif cv2.waitKey(1) & 0xff == ord('l'):
                    r -= 1
                    if r < 0:
                        r = 0
                    camera.release()
                    camera = cv2.VideoCapture(r)
                else:
                    (grabbed, img) = camera.read()
                    cv2.imshow("sources", img)
            camera.release()
            cv2.destroyWindow("sources")
            


    def calibrate(self, chessBoardShape, imgDir, imgFormat = ".jpg", picCutType = "a"):
        cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
        cv2.resizeWindow('img', 800, 600)
        obj_points = [] # 3D points
        img_points = [] # 2D points
        criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.0001)
        objp = np.zeros((chessBoardShape[0] * chessBoardShape[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:chessBoardShape[0], 0:chessBoardShape[1]].T.reshape(-1, 2)
        images = glob.glob(imgDir + "/*" + imgFormat)
        for filename in images:
            img = pictureCut(cv2.imread(filename), picCutType)
            cv2.imshow('img', img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            size = gray.shape[::-1]
            ret, corners = cv2.findChessboardCorners(gray, (chessBoardShape[0], chessBoardShape[1]), None)
            print(ret)
            if ret:
                obj_points.append(objp)
                corners2 = cv2.cornerSubPix(gray, corners, ((chessBoardShape[0] - 1) // 2, (chessBoardShape[1] - 1) // 2), (-1, -1), criteria) # 在原角点的基础上寻找亚像素角点
                if [corners2]:
                    img_points.append(corners2)
                else:
                    img_points.append(corners)
                cv2.drawChessboardCorners(img, (chessBoardShape[0], chessBoardShape[1]), corners, ret)
                cv2.imshow('img', img)
                cv2.waitKey(10)
        print(len(img_points))
        cv2.destroyAllWindows()
        ret, self.intrinsic_matrix, self.distortion_cofficients, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, size, None, None)
        return self.intrinsic_matrix, self.distortion_cofficients
    
    def setStoreDir(self, store_dir):
        self.store_dir =store_dir

    def unisort(self, img):
        h, w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(self.intrinsic_matrix, self.distortion_cofficients, (w, h), 1, (w, h))#显示更范围的图片（正常重映射之后会删掉一部分图像）
        dst = cv2.undistort(img, self.intrinsic_matrix, self.distortion_cofficients, None, newcameramtx)
        x,y,w,h = roi
        return dst[y:y+h,x:x+w]
        

            

            