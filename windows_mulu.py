#!/usr/bin/python
# -*- coding:gbk -*-
# import urllib2
import urllib
import os
import shutil

homedir = os.getcwd()
from os.path import join, getsize

'''
获取当前文件夹，和文件夹大小
放在要统计的文件夹下
'''
FOLDER_LIST = []


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size


def getFileSize(size):
    if size / 1024 > 1:
        if size / (1024 * 1024) > 1:
            return '%0.2fMB' % float(size / (1024 * 1024))
        else:
            return '%0.2fKB' % float(size / 1024)
    else:
        return '%0.2fKB' % float(size / 1024)


def sort(A, num):
    for i in range(len(A)):
        (A[i][0], A[i][num]) = (A[i][num], A[i][0])
    A.sort(reverse=True)
    for i in range(len(A)):
        (A[i][0], A[i][num]) = (A[i][num], A[i][0])


for i in os.listdir('.'):
    if os.path.isdir(i):
        fileSize = getdirsize(homedir + '\\' + i)
        FOLDER_LIST.append([homedir + '\\' + i, fileSize])

        print(homedir + '\\' + i + '\t文件大小:%s' % (getFileSize(float(fileSize))))


sort(FOLDER_LIST, 1)
print('*********************排序后*********************')

for arr in FOLDER_LIST:
    print(arr[0] + '\t文件大小:%s' % (getFileSize(float(arr[1]))))

    print('---------------------------------------------------------')


os.system('pause')
