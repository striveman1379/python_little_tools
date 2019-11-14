# -*- coding:utf-8 -*-

import xlwt
import os

"""
将数据写入excel的脚本，简单版
"""

class ExcelWriteHelper:

    @staticmethod
    def write(title,data,excel_name,save_path=os.getcwd()):
        """

        :param title: sheet中的标题
        :param data: 标题对应的内容数据
        :param excel_name: excel的文件名
        :param save_path: excel文件的存放路径，默认为当前路径
        :return:
        """
        order_num = 0
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)
        for i in range(len(title)):
            sheet.write(0, i, title[i])
        for info in data:
            order_num+=1
            for j in range(len(info)):
                sheet.write(order_num,j,info[j])

        book.save(os.path.join(save_path,excel_name))

if __name__ == '__main__':
    title = ["姓名", "年龄", "性别", "国籍", "职业"]
    data=[["张三","20","男","中国","工程师"],
          ["李四", "30", "男", "中国", "工程师"],
          ["王五", "43", "男", "中国", "刀客"]
          ]
    excel_name="infomation3.xlsx"
    ExcelWriteHelper.write(title,data,excel_name,save_path=os.getcwd())
