# -*- coding:utf-8 -*-

import tarfile
import os

"""
压缩某个目录下所有文件
"""

def compress_file(tarfilename, dirname):
    #tarfilename是压缩包名字，dirname是要打包的目录
    if os.path.isfile(dirname):
        with tarfile.open(tarfilename, 'w') as tar:
            tar.add(dirname)

    else:
        with tarfile.open(tarfilename, 'w') as tar:
            for root, dirs, files in os.walk(dirname):
                for single_file in files:
                    if single_file != tarfilename:
                        filepath = os.path.join(root, single_file)
                        tar.add(filepath)


dirname=r"F:\surfing_test\json数据"

compress_file('test1.tar', dirname)
