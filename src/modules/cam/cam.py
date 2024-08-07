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
    def __init__(self,stereo = True ,*args) -> None:
        # args[0] == ParamDir

        if len(args) == 1:
            self.param = np.load(args[0] + '/param.npy', allow_pickle = True).all()
            points = np.load(args[0] + '/points.npz', allow_pickle = True)
            self.img_points, self.img_points_l, self.img_points_r, self.obj_points = points.get('arr_0'), points.get('arr_1'), points.get('arr_2'), points.get('arr_3')
            if not os.path.exists(self.param['store_dir']):
                os.mkdir(self.param['store_dir'])
            return
        elif len(args) > 1:
            return
        self.param = {'mtx_l':[],
                      'mtx_r':[], 
                      'mtx' : [],
                      'dst' : (), 
                      'R' : [],
                      'T' : [],
                      'E' : [],
                      'F' : [],
                      'source' : 0, 
                      'store_dir' : './pics', 
                      'resolution' : (1920, 1080),
                      'stereo' : stereo}
        if not os.path.exists(self.param['store_dir']):
            os.mkdir(self.param['store_dir'])

    def saveParam(self, ParamDir):
        if not os.path.exists(ParamDir):
                os.mkdir(ParamDir)
        np.save(ParamDir + '/param', self.param)
        np.savez(ParamDir + '/points', self.img_points, self.img_points_l, self.img_points_r, self.obj_points)
    
    def setResolution(self, resolution):
        self.param['resolution'] = resolution

    def setIntrinsicMatrix(self, IntrinsicMatrix):
        self.param['mtx'] = IntrinsicMatrix

    def setDistortionCofficients(self, DistortionCofficients):
        self.param['dst'] = DistortionCofficients

    def setStoreDir(self, store_dir):
        self.param['store_dir'] =store_dir
        if not os.path.exists(self.param['store_dir']):
            os.mkdir(self.param['store_dir'])

    def getSource(self):
        return self.param['source']
    
    def capture(self):
        camera = cv2.VideoCapture(self.param['source'])
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.param['resolution'][0])
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.param['resolution'][1])
        i = 0
        c = 0
        while not camera.isOpened():
            cv2.waitKey(10)
            c += 1
            if c>=1000:
                return False
        cv2.namedWindow('capture', cv2.WINDOW_KEEPRATIO)
        cv2.resizeWindow('capture', 800, 600)
        while True:
            (grabbed, img) = camera.read()
            cv2.imshow('capture', img)
            if cv2.waitKey(1) & 0xff == ord('c'):
                filename = str(self.param['store_dir'] + '/' + str(i) + '.jpg')
                if not cv2.imwrite(filename, img):
                    print("Error To Store " + filename)
                    i -= 1
                i += 1
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        cv2.destroyWindow("capture")
        return True

    def setSource(self, *args):
        # args[0] == source

        if len(args) == 1:
            self.param['source'] = args[0]
            return True
        elif len(args) > 1:
            return False
        camera = cv2.VideoCapture(self.param['source'])
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.param['resolution'][0])
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.param['resolution'][1])
        r = 0
        if not camera.isOpened():
            return False
        else:
            cv2.namedWindow('sources', cv2.WINDOW_KEEPRATIO)
            cv2.resizeWindow('sources', 800, 600)
            while True:
                if cv2.waitKey(1) & 0xff == ord('f'):
                    self.param['source'] = r
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
        self.obj_points = [] # 3D points
        self.img_points = [] # 2D points
        self.img_points_l = []
        self.img_points_r = []
        criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.0001)
        objp = np.zeros((chessBoardShape[0] * chessBoardShape[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:chessBoardShape[0], 0:chessBoardShape[1]].T.reshape(-1, 2)
        images = glob.glob(imgDir + "/*" + imgFormat)
        if not self.param['stereo']:
            for filename in images:
                img = pictureCut(cv2.imread(filename), picCutType)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                size = gray.shape[::-1]
                ret, corners = cv2.findChessboardCorners(gray, (chessBoardShape[0], chessBoardShape[1]), None)
                print(ret, filename)
                if ret:
                    self.obj_points.append(objp)
                    corners2 = cv2.cornerSubPix(gray, corners, ((chessBoardShape[0] - 1) // 2, (chessBoardShape[1] - 1) // 2), (-1, -1), criteria) # 在原角点的基础上寻找亚像素角点
                    if [corners2]:
                        self.img_points.append(corners2)
                    else:
                        self.img_points.append(corners)
            print(len(self.img_points))
            cv2.destroyAllWindows()
            ret, self.param['mtx'], self.param['dst'], rvecs, tvecs = cv2.calibrateCamera(self.obj_points, self.img_points, size, None, None)
            return self.param['mtx'], self.param['dst']
        else:
            for filename in images:
                img = cv2.imread(filename)
                img_l, img_r = pictureCut(img, 'l'), pictureCut(img, 'r')
                gray_l = cv2.cvtColor(img_l, cv2.COLOR_BGR2GRAY)
                gray_r = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)
                size = gray_l.shape[::-1]
                ret_l, corners_l = cv2.findChessboardCorners(gray_l, (chessBoardShape[0], chessBoardShape[1]), None)
                ret_r, corners_r = cv2.findChessboardCorners(gray_r, (chessBoardShape[0], chessBoardShape[1]), None)
                print(ret_l, ret_r, filename)
                if ret_l and ret_r:
                    self.obj_points.append(objp)
                    corners_l = cv2.cornerSubPix(gray_l, corners_l, ((chessBoardShape[0] - 1) // 2, (chessBoardShape[1] - 1) // 2), (-1, -1), criteria)
                    corners_r = cv2.cornerSubPix(gray_r, corners_r, ((chessBoardShape[0] - 1) // 2, (chessBoardShape[1] - 1) // 2), (-1, -1), criteria)
                    self.img_points_l.append(corners_l)
                    self.img_points_r.append(corners_r)
            print(len(self.img_points_l))
            ret_l, self.param['mtx_l'], self.param['dst_l'], rvecs_l, tvecs_l = cv2.calibrateCamera(self.obj_points, self.img_points_l, size, None, None)
            ret_r, self.param['mtx_r'], self.param['dst_r'], rvecs_r, tvecs_r = cv2.calibrateCamera(self.obj_points, self.img_points_r, size, None, None)

            flags = cv2.CALIB_FIX_INTRINSIC
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 100, 1e-5)

            
            ret, self.param['mtx_l'], self.param['dst_l'], self.param['mtx_r'], self.param['dst_r'], self.param['R'], self.param['T'], self.param['E'], self.param['F'] = cv2.stereoCalibrate(
            self.obj_points, 
            self.img_points_l, self.img_points_r, 
            self.param['mtx_l'], self.param['dst_l'], 
            self.param['mtx_r'], self.param['dst_r'], 
            gray_l.shape[::-1], criteria=criteria, flags=flags)

    def rectify(self, img):
        self.param['R1'], self.param['R2'], self.param['P1'], self.param['P2'], Q, roi1, roi2 = cv2.stereoRectify(self.param['mtx_l'], self.param['dst_l'], self.param['mtx_r'], self.param['dst_r'], self.param['resolution'], self.param['R'], self.param['T'])
        img_l = pictureCut(img, 'l')
        img_r = pictureCut(img, 'r')
        h, w = img_l.shape[:2]

        mapl1, mapl2 = cv2.initUndistortRectifyMap(self.param['mtx_l'], self.param['dst_l'], self.param['R1'], self.param['P1'], (w, h), cv2.CV_32FC1)
        mapr1, mapr2 = cv2.initUndistortRectifyMap(self.param['mtx_r'], self.param['dst_r'], self.param['R2'], self.param['P2'], (w, h), cv2.CV_32FC1)
        rectified_l = cv2.remap(img_l, mapl1, mapl2, cv2.INTER_LINEAR)
        rectified_r = cv2.remap(img_r, mapr1, mapr2, cv2.INTER_LINEAR)
        return rectified_l, rectified_r
    
    def unisort(self, img):
        h, w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(self.param['mtx'], self.param['dst'], (w, h), 1, (w, h))#显示更范围的图片（正常重映射之后会删掉一部分图像）
        dst = cv2.undistort(img, self.param['mtx'], self.param['dst'], None, newcameramtx)
        x,y,w,h = roi
        return dst[y:y+h,x:x+w]