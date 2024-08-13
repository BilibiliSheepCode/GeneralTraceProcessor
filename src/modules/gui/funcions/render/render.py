import numpy as np
from scipy.optimize import curve_fit
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D
from PySide6.QtWidgets import QWidget
class render:
    def __init__(self) -> None:
        pass
    def render(self, parent : QWidget):
        fig = plt.figure()
        # x=np.random.random(100)  * 20                         #从数据导入
        # y=np.zeros(100)                          #同上
        # z=x**2#+np.random.normal(0,0.1,size=100)                  #这个有点麻烦
        x, y, z = np.array([0,1,0.5,1,-0.5,-1]),np.array([1,0,0.5,0,1.5,2]),np.array([0,0,1,6.86,4,7.63])
        # data=np.array([x,y,z]).T
        # def func(xy,a,b,c,d,e,f):
        #     x,y=xy
        #     return a+b*x+c*y+d*x**2+e*y**2+f*x*y    #这好像只是个抛物线，应该是函数原型（？）
        # popt,pcov=curve_fit(func,(x, y),z)
        ax=fig.add_subplot( 111,projection='3d')
        ax.scatter(x, y,z, color='blue')
        x_range=np.linspace(0,10,1000)
        y_range=np.linspace(0,10,1000)
        X,Y=np.meshgrid(x_range,y_range)
        # Z=func((X,Y), *popt)
        # ax.plot_surface(X,Y,Z,color='red',alpha=0.5)
        # ax.set_xlabel('X')
        # ax.set_ylabel('Y')
        # ax.set_zlabel('Z')

        # # A = np.column_stack((x,y,np.ones(x.shape)))
        # # B = z
        # # coefficients = np.linalg.lstsq(A, B, rcond=None)[0]
        # # Z_ = coefficients[0] * X + coefficients[1] * Y + coefficients[2]
        # # ax.plot_surface(X, Y, Z_, alpha = 0.5, color = 'cyan')

        A = np.array([[sum(x ** 2), sum(x * y), sum(x)],
              [sum(x * y), sum(y ** 2), sum(y)],
              [sum(x), sum(y), 100]])

        B = np.array([[sum(x * z), sum(y * z), sum(z)]])
        C = np.linalg.solve(A,B.T) #@ B.T
        Z_ = C[0] * X + C[1] * Y + C[2]
        ax.plot_surface(X, Y, Z_, alpha = 0.5, color = 'cyan')

        canvas = FigureCanvasQTAgg(fig)
        toolbar=NavigationToolbar(canvas, parent)
        return canvas, toolbar
