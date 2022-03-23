import pandas as pd
import geopandas
import matplotlib.pyplot as plt
# world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# world.plot()
# plt.show()
# china_nine = geopandas.read_file(r"geojson/九段线GS（2019）1719号.geojson")
china = geopandas.read_file('china.json')
fig, ax = plt.subplots(figsize=(12, 8), dpi=80)
ax = china.plot(ax=ax, column='number')
# ax = china_nine.plot(ax=ax)
plt.show()