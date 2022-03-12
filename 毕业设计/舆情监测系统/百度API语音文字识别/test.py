﻿# _*_coding:utf_8_*_
# 代码仓库 was created by zy on 2022/3/11 18:16
#识别文字并生成音频文件
import pyttsx3

# teacher = pyttsx3.init()
# teacher.say('Hello World!')
# teacher.runAndWait()
#朗读中文
# msg = '''周奕帆，你在干什么呀？'''
# teacher = pyttsx3.init()
# teacher.say(msg)
# teacher.runAndWait()
#调节语速
# import pyttsx3
# msg = '''盼望着，盼望着，东风来了，春天的脚步近了。
#  一切都像刚睡醒的样子，欣欣然张开了眼。山朗润起来了，水涨起来了，太阳的脸红起来了。
# #小草偷偷地从土里钻出来，嫩嫩的，绿绿的。园子里，田野里，瞧去，一大片一大片满是的。坐着，躺着，打两个滚，踢几脚球，赛几趟跑，捉几回迷藏。风轻悄悄的，草软绵绵的。
# # 桃树、杏树、梨树，你不让我，我不让你，都开满了花赶趟儿。红的像火，粉的像霞，白的像雪。花里带着甜味儿，闭了眼，树上仿佛已经满是桃儿、杏儿、梨儿。花下成千成百的蜜蜂嗡嗡地闹着，大小的蝴蝶飞来飞去。野花遍地是：杂样儿，有名字的，没名字的，散在花丛里，像眼睛，像星星，还眨呀眨的。
# # “吹面不寒杨柳风”，不错的，像母亲的手抚摸着你。风里带来些新翻的泥土的气息，混着青草味儿，还有各种花的香，都在微微润湿的空气里酝酿。鸟儿将巢安在繁花嫩叶当中，高兴起来了，呼朋引伴地卖弄清脆的喉咙，唱出宛转的曲子，跟轻风流水应和着。牛背上牧童的短笛，这时候也成天在嘹亮地响着。
# # 雨是最寻常的，一下就是三两天。可别恼。看，像牛毛，像花针，像细丝，密密地斜织着，人家屋顶上全笼着一层薄烟。树叶儿却绿得发亮，小草也青得逼你的眼。傍晚时候，上灯了，一点点黄晕的光，烘托出一片这安静而和平的夜。在乡下，小路上，石桥边，有撑起伞慢慢走着的人；还有地里工作的农民，披着蓑戴着笠。他们的草屋，稀稀疏疏的，在雨里静默着。
# # 天上风筝渐渐多了，地上孩子也多了。城里乡下，家家户户，老老小小，也赶趟儿似的，一个个都出来了。舒活舒活筋骨，抖擞抖擞精神，各做各的一份儿事去，“一年之计在于春”；刚起头儿，有的是工夫，有的是希望。
# # 春天像刚落地的娃娃，从头到脚都是新的，它生长着。
# # 春天像小姑娘，花枝招展的，笑着，走着。
# # 春天像健壮的青年，有铁一般的胳膊和腰脚，他领着我们上前去。...'''
# teacher = pyttsx3.init()
# rate = teacher.getProperty('rate')
# teacher.setProperty('rate', rate - 50)
# teacher.say(msg)
# teacher.runAndWait()
# #变换声音
# import pyttsx3
# msg = '''list index out of range...'''
# teacher = pyttsx3.init()
# voices = teacher.getProperty('voices')
# for i in voices:
#     teacher.setProperty('voice',i.id)
#     teacher.say(msg)
#     teacher.runAndWait()

def use_pyttsx3():
    # 创建对象
    engine = pyttsx3.init()
    # 获取当前语音速率
    rate = engine.getProperty('rate')
    print(f'语音速率：{rate}')
    # 设置新的语音速率
    engine.setProperty('rate', 200)
    # 获取当前语音音量
    volume = engine.getProperty('volume')
    print(f'语音音量：{volume}')
    # 设置新的语音音量，音量最小为 0，最大为 1
    engine.setProperty('volume', 1.0)
    # 获取当前语音声音的详细信息
    voices = engine.getProperty('voices')
    print(f'语音声音详细信息：{voices}')
    # 设置当前语音声音为女性，当前声音不能读中文
    engine.setProperty('voice', voices[1].id)
    # 设置当前语音声音为男性，当前声音可以读中文
    engine.setProperty('voice', voices[0].id)
    # 获取当前语音声音
    voice = engine.getProperty('voice')
    print(f'语音声音：{voice}')
    # 语音文本
    path = 'test.txt'
    with open(path, encoding='utf-8') as f_name:
        words = str(f_name.readlines()).replace(r'\n', '')
    # 将语音文本说出来
    engine.say(words)
    engine.runAndWait()
    engine.stop()


if __name__ == '__main__':
    use_pyttsx3()
