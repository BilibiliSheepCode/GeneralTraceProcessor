import yaml
import numpy as np
from scipy.optimize import curve_fit
import matlotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
n=int(input())
#pos_all=np.random.rand(3,n)    #sheepcode说是坐标集 或许我需要的是x，y，z的参数
x=np.random.random(100)                                #从数据导入
y=np.random.random(100)                                   #同上
z=np.sin(x,y)+np.random.normal(0,0.1,size=100)                  #这个有点麻烦
data=np.array([x,y,z]).T
def func(xy,a,b,c,d,e,f):
    x,y=xy
    return a+b*x+c*y+d*x**2+e*y**2+f*x*y    #这好像只是个抛物线，应该是函数原型（？）
popt,pcov=curve_fit(func,(x, y),z)
fig=plt.figure()
ax=fig.add_subplot( 111,projection='3d')
ax.scatter(x, y,z, color='blue')
x_range=np.linspace(e,1,50)
y_range=np.linspace(0,1,50)
X,Y=np.meshgrid(x_range,y_range)
Z=func((X,Y), *popt)
ax.plot_surface(X,Y,Z,color='red',alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('z')
plt.show()
