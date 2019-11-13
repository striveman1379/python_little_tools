# -*- coding:utf-8 -*-


'''
将全部原始txt修改为json格式，如已经是json格式则忽略
用于处理需要上平台的格式不规范的数据

click为python的一个命令行工具
使用： $ python3 json_txt.py 目标路径
'''

import os
import json
import click


@click.option("--packages_path", "-p", help="输入包的路径")

@click.command()
def txt_json(packages_path):
    '''
        将packages_path中的所有包下的原始txt修改为json格式，如已经是json格式则忽略
        如txt不是json格式，则txt中只有原始文本，将其修改为{"filename":"文件名.wav.enc","length":"","text":"文本"}格式，
        "length"字段暂时为空。
        不会修改info文件的内容

        packages_path: 包含包的目录路径
        return: None
        '''
    for root, dirs, files in os.walk(packages_path):
        for file in files:
            file_txt=os.path.join(root, file)
            if file.endswith(".txt"):

                with open(file_txt, "r+", encoding="utf-8") as f:
                    filename=file[:-3]+"wav"
                    txt_content = f.read()
                    if not is_json(txt_content):
                        f.truncate(0)
                        f.seek(0)
                        text=txt_content.strip()
                        f.write("{\"filename\":\"%s\",\"length\":\"\",\"text\":\"%s\"}"%(filename,text))


def is_json(txt_content):
    '''
    判断txt_content是否是json格式的字符串，如已经是json格式则忽略
    content: 原始文本内容
    return: bool
    '''
    try:
        json.loads(txt_content.strip())
        return True
    except:
        return False

txt_json()
