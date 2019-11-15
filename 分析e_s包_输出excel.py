# -*- coding:utf-8 -*-

'''
对目录以及目录中的文件进行分析

统计文件数量，分类，读取文件内容，并将统计信息写入到excel文件中
'''



import os, glob,json,fnmatch
import os.path as path
import xlwt
import click


def info_content_handler(info):
    if len(info)==0:
        info="""{"age":0,"gender":"无","phone":"0","name":"无","nativePlace":"无"}"""
    try:
        json_data = json.loads(info)  # type:dict
        #info_values = [str(v) for v in list(json_data.values())]
        sex= json_data["sex"] if "sex" in json_data else json_data["gender"]
        info = str(json_data["age"])+","+sex
    except Exception as e:
        print(e)
        pass

    return info




class Package:
    # def __init__(self):
    #     self.package_path = ''                          #包路径
    #     self.is_include_wav_folder = False             #是否是包含wav的文件夹
    #     self.android_txt_files = []                     #安卓文本列表
    #     self.android_wav_files = []                     #安卓音频列表
    #
    #     self.ios_txt_files = []                         #ios文本列表
    #     self.ios_wav_files = []                         #ios音频列表

    def nums(self,packages_path):
        filepath_list=[]
        files_list=[]
        info_list=[]
        packages_name=os.path.basename(packages_path)
        if os.path.isdir(packages_path):  # 判断e+s包名路径是否是目录
            # print(packages_path)
            for root, dirs, files in os.walk(packages_path):  # root为每一层的父路径，dirs为当前路径下的N个目录，files为单个文件
                # print(files)

                for file_1 in files:
                    file_path = os.path.join(root, file_1)  # 文件的路径
                    # print(file_path)
                    filepath_list.append(file_path)
        # print(filepath_list)
        for file_path in filepath_list:
            file_name = os.path.basename(file_path)
            # print(file_name)
            files_list.append(file_name)
            if "info.txt" in file_path:
                # info_path=files_list
                info_list.append(file_path)

        info_file_path=info_list[0]

        android_txt_files = [name for name in files_list if fnmatch.fnmatch(name, "*a*.txt")]
        android_wav_files = [name for name in files_list if fnmatch.fnmatch(name, "*a*.wav")]
        ios_txt_files = [name for name in files_list if fnmatch.fnmatch(name, "*i*.txt") and not "info" in name]
        ios_wav_files = [name for name in files_list if fnmatch.fnmatch(name, "*i*.wav")]

        # print(android_txt_files)

        android_txt_file_count = len(android_txt_files)  # 安卓文本条数
        android_wav_file_count = len(android_wav_files)  # 安卓音频条数

        ios_txt_file_count = len(ios_txt_files)  # ios文本条数
        ios_wav_file_count = len(ios_wav_files)  # ios音频条数

        txt_count=android_txt_file_count+ios_txt_file_count
        wav_count=android_wav_file_count+ios_wav_file_count

        device = "未知"

        if android_wav_file_count > ios_wav_file_count:
            device = "安卓"
        elif ios_wav_file_count > android_wav_file_count:
            device = "iOS"
        elif android_wav_file_count == ios_wav_file_count:
            device = "无法推算"

        info_file_content = ""
        if len(info_file_path) >= 1:
            try:
                with open(info_file_path, "r", encoding="utf-8") as f:
                    info_file_content = f.read()
                    info_file_content = info_content_handler(info_file_content)  # 读取info.txt中的内容
            except:
                info_file_content = "无法获取info信息"


        # print(info_file_path)
        print(packages_name,device,txt_count,android_txt_file_count,ios_txt_file_count,wav_count, android_wav_file_count, ios_wav_file_count,info_file_content)
        return [packages_name,device,txt_count,android_txt_file_count,ios_txt_file_count,wav_count, android_wav_file_count, ios_wav_file_count,info_file_content]

title=['包名', '设备', 'txt条数', 'android_txt条数', 'ios_txt条数','音频条数', 'android_wav条数', 'ios_wav条数','info']

def write(packages_full_path):
    order_num = 0
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)
    for i in range(len(title)):
        sheet.write(0, i, title[i])
    for packages in os.listdir(packages_full_path):
        order_num+=1
        packages_path=os.path.join(packages_full_path,packages)
        package = Package()  # 调用Package类来对包进行分析处理
        data=package.nums(packages_path)
        for j in range(len(data)):
            sheet.write(order_num, j, data[j])
    book.save("ios_es.xls")

if __name__ == '__main__':
    packages_full_path="/DATA/20170002/原始数据/hege/ios/ios_es"
    write(packages_full_path)
