import json
import random
import sys
import os
from bokeh.plotting import curdoc, figure
from bokeh.models import GeoJSONDataSource
from bokeh.io import show
#拿地图的网站
#http://datav.aliyun.com/portal/school/atlas/area_selector#&lat=33.521903996156105&lng=104.29849999999999&zoom=3
# # 读入中国地图数据并传给GeoJSONDataSource
# with open("china.json", encoding="utf8") as f:
#     geo_source = GeoJSONDataSource(geojson=f.read())
# # 设置一张画布
# p = figure(width=500, height=500)
# # 使用patches函数以及geo_source绘制地图
# p.patches(xs='xs', ys='ys', source=geo_source)
# show(p)
with open("河南省.json", encoding="utf-8-sig") as f:
    data = json.loads(f.read())

# 判断是不是  北京地区数据
def isBeijing(district):
    if 'beijing' in district['properties']['woe-name'].lower():
        return True
    return False

# data['features'] = list(filter(isInLondon, data['features']))
# 过滤数据
# 为每一个地区增加一个color属性
for i in range(len(data['features'])):
    data['features'][i]['properties']['color'] = ['red', 'blue', 'yellow', 'orange', 'gray', 'purple'][i % 6]
    data['features'][i]['properties']['number'] = random.randint(0, 20_000)
geo_source = GeoJSONDataSource(geojson=json.dumps(data))
p = figure(width=2000, height=2000, tooltips="@name, number: @number")
p.patches(xs='xs', ys='ys', fill_alpha=0.7,
          line_color='white',
          line_width=0.5,
          color="color",  # 增加颜色属性，这里的"color"对应每个地区的color属性
          source=geo_source)
p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)