# -*- coding:utf-8 -*-


'''
此脚本的作用为将源目录下的指定类型的文件复制到自定义的目录下，文件类型可自定义，手动修改
'''

import os
import shutil

def desfile(src_dir,dst_dir):

    countFile = 0
    for root,dirs,files in os.walk(src_dir):
        for each_file in files:
            #根据后缀判断所要移动的文件类型
            if each_file.endswith('.flv'):
                file_fullpath = os.path.join(root,each_file)
                #复制路径为src的文件至路径dst，复制文件内容、权限及修改时间等信息。如dst是一个文件夹，文件src会复制到文件夹内，文件名与src的文件名一致。返回dst
                shutil.copy2(file_fullpath, dst_dir)
                countFile+=1

    print('所移动的文件数量为：',countFile)

if  __name__ == '__main__':
    src_dir = r'F:\学习仓库\计算机科学速成课'                       #文件所存放的目录
    dst_dir = r'F:\学习仓库\Crash Course Computer Science'         #文件将要移动到的目录
    desfile(src_dir, dst_dir)

