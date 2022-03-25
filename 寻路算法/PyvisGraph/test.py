# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/18 16:19
#公司电脑
import sys

sys.path.append("C:/Users/Administrator/python/")
from Putils import logger as log
from Putils import plotutil as  plt
from shapely.geometry import Polygon, Point,LineString
import pyvisgraph as vg

def generate_grid(lx, ly, pm, fm, cm, resolution, offsetx, offsety,external=0.1):
    # ax = plt.create_ax()
    res = np.zeros((lx, ly))
    for i in range(0, lx):
        for j in range(0, ly):
            current_x = i * resolution + offsetx
            current_y = j * resolution + offsety
            bb = box(current_x, current_y, current_x + resolution, current_y + resolution)
            # plt.draw_polygon(ax, bb, "r", 'w', 1)
            if bb.within(pm):
                # plt.draw_polygon(ax, bb, "m", 'w', 1)
                    # plt.draw_polygon(ax, bb, "k", 'w', 1)
                for jian in fm:
                    if bb.intersects(jian.buffer(external,cap_style=2, join_style=2)):
                        # xs_2, ys_2 = bb.boundary.xy
                        # plt.plot(xs_2, ys_2, 'chocolate')
                        # plt.draw_polygon(ax, bb, "k", 'w', 1)
                        res[i][j] = 1
                        break
                for he in cm:
                    if bb.intersects(he):
                        # xs_2, ys_2 = bb.boundary.xy
                        # plt.plot(xs_2, ys_2, 'chocolate')
                        # plt.draw_polygon(ax, bb, "r", 'w', 1)
                        res[i][j] = 0
                        break
                if bb.intersects(pm.boundary.buffer(1)):
                    res[i][j] = 1
                # 最终合理的条件
                # if not tag:
                #     res[i][j] = 1
    # ax.autoscale_view()
    # plt.show()
    return res

if __name__ == "__main__":
       # log.critical("你好")
       # print('\033[1;35;0m字体变色，但无背景色 \033[0m')  # 有高亮 或者 print('\033[1;35m字体有色，但无背景色 \033[0m')
       # print('\033[1;45m 字体不变色，有背景色 \033[0m')  # 有高亮
       # print('\033[1;35;46m 字体有色，且有背景色 \033[0m')  # 有高亮
       # print('\033[0;35;46m 字体有色，且有背景色 \033[0m')  # 无高亮
       # polys = [[vg.Point(0.0,1.0), vg.Point(3.0,1.0), vg.Point(1.5,4.0)],
       #        [vg.Point(4.0,4.0), vg.Point(7.0,4.0), vg.Point(5.5,8.0)]]
       # g = vg.VisGraph()
       # g.build(polys)
       # shortest = g.shortest_path(vg.Point(1.5,0.0), vg.Point(4.0, 6.0))
       # print(shortest)
       # poly1=Polygon([Point(0.0,1.0),Point(3.0,1.0),Point(1.5,4.0)])
       # poly2=Polygon([Point(4.0,4.0),Point(7.0,4.0),Point(5.5,8.0)])
       # ax = plt.create_ax()
       # plt.draw_polygon(ax,Point(1.5,0.0).buffer(0.1),"m","g")
       # plt.AddText(ax,Point(1.5,0.0),"起点")
       # plt.draw_polygon(ax,Point(4.0, 6.0).buffer(0.1),"m","g")
       # plt.AddText(ax,Point(4.0, 6.0),"终点")
       # plt.draw_polygon(ax,poly1,"w","r",1)
       # plt.draw_polygon(ax,poly2,"w","r",1)
       # plt.draw(ax,LineString([(_.x,_.y) for _ in shortest]))
       # plt.show(ax)


# Once the visibility graph is built, it can be saved and subsequently loaded. This is useful for large graphs where build time is long. pickle is used for saving and loading.

# g.save('graph.pk1')
# g2 = vg.VisGraph()
# g2.load('graph.pk1')

# For obstacles with a large number of points, Pyvisgraph can take advantage of processors with multiple cores using the multiprocessing module. Simply add the number of workers (processes) to the build method:

# g.build(polys, workers=4)
