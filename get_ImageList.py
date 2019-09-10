# -*- coding:utf-8 -*-

import os
import re
import csv

def searchFile(search_dir):
    #使用os.walk来遍历每一层目录
    for root,dirs,files in os.walk(search_dir):
        #因为遍历后files是一个列表，所以要显示每一个文件的路径，就必须循环该文件列表，取出每一个文件
        for file_name in files:
            #用os.path.join做拼接，得到每一个文件的具体路径
            file_path=os.path.join(root,file_name)
            # print(file_path)
            #对文件全路径做切割，取出所有文件的文件夹路径
            prefix = os.path.dirname(file_path)
            # suffix = file_path.split("\\")[-1]
            # 对文件全路径做切割，取出所有文件的文件名
            suffix = os.path.basename(file_path)
            #因为要获取所有的docker-compose.yml，所以直接根据文件名做匹配
            if suffix == "docker-compose.yml":
                #新建一份csv文件，以追加的方式将结果写入到文件中
                with open(csv_file, 'a') as csv_f:
                    f_csv = csv.writer(csv_f)
                    # print(prefix)
                    # print(file_path)
                    #根据符合条件的文件绝对路径读取文件里面的内容
                    with open(file_path,'r') as f:
                        res = f.read()
                        #用re模块，根据正则匹配规则，找到所有文件对应的image
                        images = re.findall("image: .*", res)
                        #创建data变量，将文件所属的目录的路径和对象的镜像以列表的形式存放在data中
                        data = [prefix,images]
                        #将结果写入到csv文件的每一行
                        f_csv.writerow(data)



if __name__ == '__main__':
    search_dir = r"F:\安全攻防\vulhub-master"
    csv_file = r"F:\安全攻防\镜像列表.csv"
    searchFile(search_dir)


