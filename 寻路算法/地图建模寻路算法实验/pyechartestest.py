from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
# 官方网站，https://pyecharts.org/#/zh-cn/intro
from pyecharts.charts import Bar
from pyecharts import options as opts
# 设置图形主题，内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
###################################################################################
# filepath = r'C:\Users\Administrator\Desktop\myEcharts.html'
# bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#上面所有代码可用下面一句表示，支持链式
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
#     )

# bar.render(filepath)
#################################################################################################

c = (
    Map()
        .add("测试数据", [list(z) for z in zip(Faker.country, Faker.values())], "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
)
c.render_notebook()
c = (
    Map()
    .add("测试数据", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-VisualMap（中国）"),
        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
    )
)
# c.render(filepath)
c.render_notebook()