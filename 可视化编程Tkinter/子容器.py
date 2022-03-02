# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/2 21:21
from tkinter import *
#创建窗口
rview=Tk()
#标题
rview.title("东小东")
#窗口基于屏幕的坐标 +x轴+y轴
rview.geometry("+500+200")
#创建lab标签
labelx=Label(rview,text="父容器Lab",font=("宋体",30))
#显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
labelx.grid(row=0,column=1)

#----------------------------------------------------------------------------

# 创建一个子容器，其父容器为rview
monty = LabelFrame(rview, text="== 子容器标题 ==")
monty.grid(column=0, row=0,padx=5,pady=5) #设置子容器在父容器的位置


#创建子容器里的按钮1
buttonx1=Button(monty,text="按钮1",font=("宋体",20),fg="red")
buttonx1.grid(row=0,column=0) #设置按钮在子容器的位置

#创建子容器里的按钮2
buttonx2=Button(monty,text="按钮2",font=("宋体",20),fg="green")
buttonx2.grid(row=1,column=0) #设置按钮在子容器的位置

#---------------------------------------------------------------------------

#消息循环 显示窗口
rview.mainloop()
