# -*- coding: utf-8 -*-
"""
自动创建一个类
@author: rly1100
"""
import os
import xlrd

# 初始化函数
def write_init(file, name_list):
    file.write('\t' + 'def __init__(self, _json):' + '\n')

    file.write('\t' * 2 + 'self.paras = {\n')

    for item in name_list[1:]:
        file.write('\t' * 3 + '"{}":"''",\n'.format(item))
    file.write('\t' * 3 + '}\n\n')


# 属性添加
def write_property(file, name_list):
    for item in name_list[1:]:
        file.write('\t' * 2 + '@property' + '\n')
        file.write('\t' * 2 + 'def {}(self):'.format(item) + '\n')
        file.write('\t' * 3 + 'return self.paras["{}"]\n\n'.format(item))

        file.write('\t' * 2 + '@{}.setter'.format(item) + '\n')
        file.write('\t' * 2 + 'def {}(self, {}):'.format(item, item) + '\n')
        file.write('\t' * 3 + 'self.paras["{}"] = {}\n\n\n'.format(item, item))


ExcelFile = xlrd.open_workbook(r'./需求.xls')
sheet = ExcelFile.sheet_by_index(0)
name_list = []

for i in range(0, sheet.nrows):
    name_list.append(sheet.col_slice(0)[i].value)

with open('output.py', 'w') as f:
    class_name = sheet.name
    f.write("class {}:\n".format(class_name))
    write_init(f, name_list)
    write_property(f, name_list)

# from output import BaseModule

