# -*- coding:utf-8 -*-

#在嵌套模式的字典中，根据指定的key，来取其对应的值

#in_dict:需要处理的字典，target_key:目标键
#results：输出的列表，元素为目标键对应的值（必须为空列表），not_d:获取的目标类型不为dict

def get_dict_value(in_dict, target_key, results=[],not_d=True):
    for key in in_dict.keys():          #迭代当前的字典层级
        data = in_dict[key]             #将当前字典层级的第一个元素的值赋值给data
        # print(data)

        #如果当前data属于dict类型，进行回归
        if isinstance(data,dict):
            get_dict_value(data,target_key,results=results,not_d=True)

        #如果当前键与目标键相等，并且判断是否要筛选
        if key == target_key and isinstance(data,dict) != not_d:
            results.append(in_dict[key])
    return results



if __name__ == '__main__':
    dicts = {'version': '2', 'services': {'redis': {'image': 'vulhub/redis:4.0.14', 'ports': ['6379:6379']}}}
    a=get_dict_value(dicts,'ports')
    print(a)
