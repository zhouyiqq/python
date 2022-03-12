# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/11 23:00
def saveHtml(file_name, file_content):
     # 注意windows文件命名的禁用符，比如 /
     with open(file_name.replace('/', '_') + ".html", "wb") as f:
          # 写文件用bytes而不是str，所以要转码
          f.write(file_content)