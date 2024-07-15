import cv2
import glob
import os
import numpy as np

class Cam:
    __chessboard_shape = ()
    __objpoints = []
    __imgpoints = []
    def __init__(self) -> None:
        pass