# -*- coding:utf-8 -*-

'''
求两个文件的差集，文件f1和文件f2，f2文件中的内容比f1文件的多，要提取出f2文件中多余的部分
'''

f1=r"F:\surfing_test\map_txt\t3.txt"
f2=r"F:\surfing_test\map_txt\t4.txt"

def map_txt(f1,f2):

    with open(f1, 'r',encoding="utf-8") as file1:
        with open(f2, 'r',encoding="utf-8") as file2:
            different = set(file2).difference(file1)            #前面的文件为内容多的，后面的是少的

    different.discard('\n')

    with open('different00_output_file.txt', 'w',encoding="utf-8") as file_out:
        for line in different:
            file_out.write(line)

if __name__ == '__main__':
    map_txt(f1,f2)

