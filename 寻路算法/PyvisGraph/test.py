# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/18 16:19
from Putils import plotutil
import pyvisgraph as vg
polys = [[vg.Point(0.0,1.0), vg.Point(3.0,1.0), vg.Point(1.5,4.0)],
       [vg.Point(4.0,4.0), vg.Point(7.0,4.0), vg.Point(5.5,8.0)]]
g = vg.VisGraph()
g.build(polys)
shortest = g.shortest_path(vg.Point(1.5,0.0), vg.Point(4.0, 6.0))
# print(shortest)



# Once the visibility graph is built, it can be saved and subsequently loaded. This is useful for large graphs where build time is long. pickle is used for saving and loading.

# g.save('graph.pk1')
# g2 = vg.VisGraph()
# g2.load('graph.pk1')

# For obstacles with a large number of points, Pyvisgraph can take advantage of processors with multiple cores using the multiprocessing module. Simply add the number of workers (processes) to the build method:

# g.build(polys, workers=4)
