# -*- coding:utf-8 -*-

#打印进度条
import sys,time
print("打印进度条")
for i in range(20):
    sys.stdout.write("-")   #标准化输出，类似print,print默认换行
    sys.stdout.flush()      #强制刷新，将内存中的内容写入硬盘
    time.sleep(0.5)         #推迟执行的秒数
    if i==19:
        sys.stdout.write("100%")

