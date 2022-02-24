#coding='utf-8'
import xlrd
import re

def extract(inpath):
    """提取数据"""
    data = xlrd.open_workbook(inpath, encoding_override='utf-8')
    table = data.sheets()[0]#选定表
    nrows = table.nrows#获取行号
    ncols = table.ncols#获取列号
    numbers=[]
    for i in range(1, nrows):#第0行为表头
        alldata = table.row_values(i)#循环输出excel表中每一行，即所有数据
        result_0 = alldata[4]#取出正文
        numbers.append(result_0)
        #numbers.append([result_0,result_3,result_4,result_5])
    return numbers

def clean(line):
    """对一个文件的数据进行清洗"""
    rep=['【】','【','】','👍','🤝',
        '🐮','🙏','🇨🇳','👏','❤️','………','🐰','...、、','，，','..','💪','🤓',
         '⚕️','👩','🙃','😇','🍺','🐂','🙌🏻','😂','📖','😭','✧٩(ˊωˋ*)و✧','🦐','？？？？','//','😊','💰','😜','😯',
         '(ღ˘⌣˘ღ)','✧＼٩(눈౪눈)و/／✧','🌎','🍀','🐴',
         '🌻','🌱','🌱','🌻','🙈','(ง•̀_•́)ง！','🉑️','💩',
         '🐎','⊙∀⊙！','🙊','【？','+1','😄','🙁','👇🏻','📚','🙇',
         '🙋','！！！！','🎉','＼(^▽^)／','👌','🆒','🏻',
         '🙉','🎵','🎈','🎊','0371-12345','☕️','🌞','😳','👻','🐶','👄','\U0001f92e\U0001f92e','😔','＋1','🛀','🐸','🐷','➕1',
         '🌚','：：','💉','√','x','！！！','🙅','♂️','💊','👋','o(^o^)o','mei\u2006sha\u2006shi','💉','😪','😱',
         '🤗','关注','……','(((╹д╹;)))','⚠️','Ծ‸Ծ','⛽️','😓','🐵',
         '🙄️','🌕','…','😋','[]','[',']','→_→','💞','😨','&quot;','😁','ฅ۶•ﻌ•♡','😰','🎙️',
         '🤧','😫','(ง•̀_•́)ง','😁','✊','🚬','😤','👻','😣','：','😷','(*^▽^)/★*☆','🐁','🐔','😘','🍋','(✪▽✪)','(❁´ω`❁)','1⃣3⃣','(^_^)／','☀️',
	     '🎁','😅','🌹','🏠','→_→','🙂','✨','❄️','•','🌤','💓','🔨','👏','😏','⊙∀⊙！','👍','✌(̿▀̿\u2009̿Ĺ̯̿̿▀̿̿)✌',
         '😊','👆','💤','😘','😊','😴','😉','🌟','♡♪..𝙜𝙤𝙤𝙙𝙣𝙞𝙜𝙝𝙩•͈ᴗ•͈✩‧₊˚','👪','💰','😎','🍀','🛍','🖕🏼','😂','(✪▽✪)','🍋','🍅','👀','♂️','🙋🏻','✌️','🥳','￣￣)σ',
         '😒','😉','🦀','💖','✊','💪','🙄','🎣','🌾','✔️','😡','😌','🔥','❤','🏼','🤭','🌿','丨','✅','🏥','ﾉ','☀','5⃣⏺1⃣0⃣','🚣','🎣','🤯','🌺',
         '🌸',
         ]
    pattern_0=re.compile('#.*?#')#在用户名处匹配话题名称
    pattern_1=re.compile('【.*?】')#在用户名处匹配话题名称
    pattern_2=re.compile('肺炎@([\u4e00-\u9fa5\w\-]+)')#匹配@
    pattern_3=re.compile('@([\u4e00-\u9fa5\w\-]+)')#匹配@
    #肺炎@环球时报
    pattern_4=re.compile(u'[\U00010000-\U0010ffff\uD800-\uDBFF\uDC00-\uDFFF]')#匹配表情
    pattern_5=re.compile('(.*?)')#匹配一部分颜文字
    pattern_7=re.compile('L.*?的微博视频')
    pattern_8=re.compile('（.*?）')
    #pattern_9=re.compile(u"\|[\u4e00-\u9fa5]*\|")#匹配中文

    line=line.replace('O网页链接','')
    line=line.replace('-----','')
    line=line.replace('①','')
    line=line.replace('②','')
    line=line.replace('③','')
    line=line.replace('④','')
    line=line.replace('>>','')
    line=re.sub(pattern_0, '', line,0) #去除话题
    line=re.sub(pattern_1, '', line,0) #去除【】
    line=re.sub(pattern_2, '', line,0) #去除@
    line=re.sub(pattern_3, '', line,0) #去除@
    line=re.sub(pattern_4, '', line,0) #去除表情
    line=re.sub(pattern_5, '', line,0) #去除一部分颜文字
    line=re.sub(pattern_7, '', line,0) 
    line=re.sub(pattern_8, '', line,0) 
    line=re.sub(r'\[\S+\]', '', line,0) #去除表情符号
    
    for i in rep:
        line=line.replace(i,'')
    return line


if __name__ == "__main__":
    names=['12月','1月','2月','3月','4月','5月','6月']
    for name in names:
        numbers=extract('excel分月\\'+name+'.xlsx')#正文
        f=open('正文汇总分月\\'+name+'.txt','w',encoding='utf-8')
        for line in numbers:
            line=str(line)
            line=clean(line)
            f.write(line+'\n')
        f.close()


