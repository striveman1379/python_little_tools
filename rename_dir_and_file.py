# -*- coding:utf-8 -*-

'''
有时会遇到一些情况，目录及其内部文件中的一些名字"aaa"想要替换为“bbb”，故可以用此脚本来进行修改

'''

import os

list2=["ZY3244", "ZY3246"]
list1=["P00001", "P00002"]

tp=zip(list1, list2)   #针对包名建立对应关系
# print(tp)

path = "/home/changkai/test_file/test2/"   #目标路径


def rename_dir_file(path):
    for p_name in tp:                       #循环包名数组
        for dirs in os.listdir(path):
            if dirs == p_name[0]:                 #如果取到的包名和数组中的旧包名相同，就讲包名重命名
                os.rename(path+dirs, path+p_name[1])
            for root, dirnames, files in os.walk(path+p_name[1]):
                for file in files:
                    filename=file.split(dirs)       #根据包名切割文件名
                    project_name=filename[0]         #项目名
                    filename_suffix=filename[1]       #filename_suffix为包名后面的字符串
                    file_new_name=project_name+p_name[1]+filename_suffix    #新包名=项目名+新包名+包名后面的字符串
                    old_file_path = os.path.join(root, file)
                    new_file_path = os.path.join(root, file_new_name)

                    os.rename(old_file_path, new_file_path)



if __name__ == '__main__':
    rename_dir_file(path)
