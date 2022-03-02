# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/2 22:04
from numpy import pi, sin, cos, mgrid
from mayavi import mlab

# 你好
dphi, dtheta = pi/250.0, pi/250.0
[phi, theta] = mgrid[0:pi+dphi*1.5:dphi, 0:2*pi+dtheta*1.5:dtheta]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6**theta)**m7
x = r*sin(phi)*cos(theta)
y = r*cos(phi)
z = r*sin(phi)*sin(theta)

s = mlab.mesh(x, y, z)
mlab.show()


x = [[-1, 1, 1, -1, -1], [-1, 1, 1, -1, -1]]
y = [[-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
z = [[1, 1, -1, -1, 1], [1, 1, -1, -1, 1]]

s = mlab.mesh(x, y, z)
mlab.show()
