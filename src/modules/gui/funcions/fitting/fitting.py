import numpy as np
from scipy.optimize import curve_fit
class Fitting:
    def __init__(self) -> None:
        pass

    def planeFit(self, points):
        #去质心
        x, y, z = points[0] - np.mean(points[0]), points[1] - np.mean(points[1]), points[2] - np.mean(points[2])
        A = np.transpose(np.asarray([x, y, z]))
        cov_matrix = np.cov(A, rowvar=False)
        U, S, Vt = np.linalg.svd(cov_matrix)
        eigenvalues = S
        eigenvectors = Vt.T
        center =  np.mean(points, axis=1)
        X = eigenvectors[2]
        return X[0], X[1], X[2], (-X[0] * center[0] - X[1] * center[1] - X[2] * center[2])
    
    def project(self, points, A, B, C, D):
        nvector = np.array([A, B, C])
        t = - (np.dot(nvector.T, points) + D) / (A**2 + B**2 + C**2)
        return np.dot(nvector, t) + points

    def parabolaFit(self, points):
        A, B, C, D = self.planeFit(points)
        po = self.project(np.array([0,0,0]), A, B, C, D)
        pp = self.project(points, A, B, C, D)
        pr = pp - po
        vx = pr.T[0] / np.sqrt(pr.T[0]**2 + pr.T[2]**2 + pr.T[2]**2)
        vy = np.cross(vx, np.array[A, B, C] / np.sqrt(A**2 + B**2 + C**2))
        mt = np.vstack(vx, vy)
        pf = np.dot(mt, pr)
        def func(x,a,b,c):
            return a * np.power(x, 2) + b * x + c
        popt,pcov=curve_fit(func, pf[0], pf[1])
        # x = np.linspace(0,10,1000)
        # y = func(x, *popt)
        # pn = np.dot(np.hstack(x, y), mt)
        return np.array([A, B, C, D]), popt
        