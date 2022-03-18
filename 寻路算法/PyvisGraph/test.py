# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/18 16:19
#公司电脑
from Putils import plotutil as plt
from shapely.geometry import Polygon, Point,LineString
import pyvisgraph as vg
polys = [[vg.Point(0.0,1.0), vg.Point(3.0,1.0), vg.Point(1.5,4.0)],
       [vg.Point(4.0,4.0), vg.Point(7.0,4.0), vg.Point(5.5,8.0)]]
g = vg.VisGraph()
g.build(polys)
shortest = g.shortest_path(vg.Point(1.5,0.0), vg.Point(4.0, 6.0))
print(shortest)
poly1=Polygon([Point(0.0,1.0),Point(3.0,1.0),Point(1.5,4.0)])
poly2=Polygon([Point(4.0,4.0),Point(7.0,4.0),Point(5.5,8.0)])
ax = plt.create_ax()
plt.draw_polygon(ax,Point(1.5,0.0).buffer(0.1),"m","g")
plt.AddText(ax,Point(1.5,0.0),"起点")
plt.draw_polygon(ax,Point(4.0, 6.0).buffer(0.1),"m","g")
plt.AddText(ax,Point(4.0, 6.0),"终点")
plt.draw_polygon(ax,poly1,"w","r",1)
plt.draw_polygon(ax,poly2,"w","r",1)
plt.draw(ax,LineString([(_.x,_.y) for _ in shortest]))
plt.show(ax)


# Once the visibility graph is built, it can be saved and subsequently loaded. This is useful for large graphs where build time is long. pickle is used for saving and loading.

# g.save('graph.pk1')
# g2 = vg.VisGraph()
# g2.load('graph.pk1')

# For obstacles with a large number of points, Pyvisgraph can take advantage of processors with multiple cores using the multiprocessing module. Simply add the number of workers (processes) to the build method:

# g.build(polys, workers=4)
