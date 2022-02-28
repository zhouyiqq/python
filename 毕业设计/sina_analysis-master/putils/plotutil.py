import random
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from descartes.patch import PolygonPatch
from shapely.geometry import LineString, Polygon

plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体


def create_ax():
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_aspect('equal')
    # ax.autoscale_view()
    return ax


def draw(ax, obj, facecolor='w', edgecolor=None, zorder=1):
    if isinstance(obj, LineString):
        draw_line(ax, obj, edgecolor, zorder)
    elif isinstance(obj, Polygon):
        draw_polygon(ax, obj, facecolor, edgecolor, zorder)
    ax.autoscale_view()


def draw_random_merge_result(data, random_merge_result):
    for i in range(len(random_merge_result)):
        coll = random_merge_result[i]
        ax = create_ax()
        draw_division(ax, data)
        for each_park_poly in coll.ParkPoly_list:
            poly = each_park_poly.poly
            cell_multipolygon = each_park_poly.cell_multipolygon
            draw_polygon(ax, poly, random_color(), random_color(), 2)
            draw_cells_multipolygon(ax, cell_multipolygon)
        ax.autoscale_view()
        ax.set_title('park number is ' + str(coll.park_number))


def draw_division(ax, data):
    draw_polygon(ax, data.outer_vertex_poly,
                 facecolor='w', edgecolor='r', zorder=1)
    for build_poly in data.building_vertex_polys:
        draw_polygon(ax, build_poly, facecolor='w', edgecolor='b', zorder=3)


def draw_extendLine_and_rect_random_division(data):
    ax = create_ax()
    draw_division(ax, data)
    rects = data.rect_matrix_for_random_merge
    for r1 in rects:
        for r in r1:
            if r.valid:
                poly = r.poly
                draw_polygon(ax, poly, facecolor=random_color(),
                             edgecolor='w', zorder=2)

    ax.autoscale_view()


def draw_cells_multipolygon(ax, cell_multipolygon, facecolor='w', edgecolor='r', zorder=2):
    if cell_multipolygon:
        for poly in cell_multipolygon:
            patch = PolygonPatch(poly, facecolor=facecolor,
                                 edgecolor=edgecolor, zorder=zorder)
            ax.add_patch(patch)


def draw_multipoly(ax, mp, facecolor=None, edgecolor='b', zorder=1):
    for p in mp:
        if facecolor == None:
            draw_polygon(ax, p, facecolor=random_color(),
                         edgecolor=edgecolor, zorder=zorder)
        else:
            draw_polygon(ax, p, facecolor=facecolor,
                         edgecolor=edgecolor, zorder=zorder)


def draw_buildings(ax, buildings, facecolor='k', edgecolor='r', zorder=1):
    for b in buildings:
        draw_polygon(ax, b, facecolor=facecolor,
                     edgecolor=edgecolor, zorder=zorder, alpha=0.5)


def draw_polygon(ax, poly, facecolor, edgecolor, zorder=1, alpha=1.0):
    if not facecolor:
        facecolor = random_color()
    if not edgecolor:
        edgecolor = random_color()
    patch = PolygonPatch(poly, facecolor=facecolor,
                         edgecolor=edgecolor, zorder=zorder, alpha=alpha)
    ax.add_patch(patch)


def draw_line(ax, ob, color, linewidth=1):
    if ob.geom_type == 'MultiLineString':
        for each in ob:
            tmp = each.xy
            t0 = [[_ for _ in tmptmp] for tmptmp in tmp]
            ax.plot(*t0, color=color, linewidth=linewidth)
    else:
        tmp = ob.xy
        t0 = [[_ for _ in tmptmp] for tmptmp in tmp]
        ax.plot(*t0, color=color, linewidth=linewidth)


def plot_multiline_coords(ax, ob, color='#999999', zorder=1, alpha=1):
    for L in ob:
        plot_coords(ax, L)


def plot_coords(ax, ob, color='#999999', zorder=1, alpha=1):
    x, y = ob.xy
    ax.plot(x, y, 'o', color=color, zorder=zorder, alpha=alpha)


def set_title(ax, title):
    ax.set_title(title, fontproperties='SimHei', fontsize=13)
def draw_grid(x,y,gridwith=1):
    x = np.array(np.arange(0,x,gridwith))
    y = np.array(np.arange(0,y,gridwith))
    plt.xticks(x)
    plt.yticks(y)
    plt.grid(c ="r")

def show():
    plt.show()


def random_color():
    return '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])


def parallel_offset_gradually(linestring, offset, direction, join_style):
    pass


def savefig(fig, fname, dpi):
    fig.savefig('./result/' + fname + '.png', dpi=dpi, format='png')


color = ["#ef4136", "#fdb933", "#33a3dc", "#ea66a6"]


def plotLine(ax, line, _color=None):
    _color = color[random.randint(0, 3)] if _color is None else _color
    if line.type == "LineString":
        t1 = [[_ for _ in tmptmp] for tmptmp in line.xy]
        ax.plot(*t1, color=_color, linewidth=1.0, linestyle="-")
    else:
        print("画图错误:" + str(line.type))


def plotPolygon(ax, x, _color=None):
    _color = color[random.randint(0, 3)] if _color is None else _color
    ax.add_patch(PolygonPatch(x, facecolor="w",
                                   edgecolor=_color, zorder=1, alpha=1.0))
def AddText(ax,p,str_):
    ax.text(p.centroid.x, p.centroid.y, str_, ha='center', fontsize=12, color='#121a2a')