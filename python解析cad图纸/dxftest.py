# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:21:38 2022

@author: Administrator
"""

import dxfgrabber
import numpy as np
from shapely.geometry import Polygon
from shapely.geometry import Point


from shapely.geometry import shape
from shapely.geometry import mapping

from shapely.ops import unary_union
from shapely.affinity import affine_transform
from shapely.affinity import translate
from shapely.ops import split
import matplotlib.pyplot as plt
import time


dxf = dxfgrabber.readfile("清风拂翠.dxf")
'''
for layer in dxf.layers:
    if layer.linetype == 'Continuous':
        print(layer.name,layer.color,layer.linetype)
        print(layer.__dict__)
        

'''   

def plt_coor_gen(layer, line_type):
    try:
        p = layer.points
        print(p)
    except Exception as e:
        print(str(e))
        return
        
        
    # print('plot:',layer.layer)
    dimen = np.array(p).shape
    if dimen[0] <= 2:
        return 
    # print('数据维度：', dimen)
    context = {
        'type':'Polygon',
        'coordinates': ([p])
        }     
    a = shape(context)
    x , y = a.boundary.xy
    plt.plot(x, y, line_type, linewidth=0.5)

plt.axis('equal')

tag = True
count = 0




for layer in dxf.entities:
    # print(layer.__dict__)
    # print(layer.points)
    

    if layer.layer == 'G-模块轮廓线':  
        plt_coor_gen(layer, 'r')
        break
        
    
    if layer.layer == 'B-围边':  
        plt_coor_gen(layer, 'b')
        
        
  
        

        
        
        
        

names = []
for layer in dxf.entities:
    names.append(layer.layer)

FFPlane_cent = []

    
# grouping

# 定义一个参数组合


    
       
        
        
    
   




