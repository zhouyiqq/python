import folium
# 绘制边界
import json
import pandas as pd

# define the world map
world_map = folium.Map()
# display world map
world_map
# df = pd.read_csv(r'plotly-choropleth-mapbox-demo-master/data.csv')
# # read china border
# with open(r"plotly-choropleth-mapbox-demo-master/china_province.geojson", encoding='utf8') as f:
#     china = json.load(f)
#
# chn_map = folium.Map(location=[40, 100], zoom_start=4)
#
# folium.Choropleth(
#     geo_data=china,
#     name="choropleth",
#     data=df,
#     columns=["地区", "确诊"],
#     key_on="properties.NL_NAME_1",
#     fill_color="YlGn",
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name="新冠确诊",
# ).add_to(chn_map)
#
# folium.LayerControl().add_to(chn_map)
