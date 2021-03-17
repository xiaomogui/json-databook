
import time

def formatTime(longtime):
    # 格式化时间的函数
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))

def formatByte(number):
    # 格式化文件大小的函数
    for(scale, label) in [(1024*1024*1024,"GB"),(1024*1024,"MB"),(1024,"KB")]:
        if number>=scale:
            return  "%.2f %s" %(number*1.0/scale,lable)
        elif number ==1:
            return  "1字节"
        else:
            #小于1字节
            byte = "%.2f" % (number or 0)
    return (byte[:-3]) if byte.endswith(".00") else byte + "字节"
