from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError


from django.shortcuts import render, HttpResponse
import random
# from utils.tencent.sms import send_sms_single


# 腾讯云短信应用的 app_id
TENCENT_SMS_APP_ID = 1400470623

# 腾讯云短信应用的 app_key
TENCENT_SMS_APP_KEY = "668c148d4b5a1e1e8f9b62ed899a29b3"

# 腾讯云短信签名内容
TENCENT_SMS_SIGN = "我的CODING的杂谈"

TENCENT_SMS_TEMPLATE = {
    'register': 842633,
    'login': 842634
}


# Create your views here.
def send_sms_single(phone_num, template_id, template_param_list):
    """
    单条发送短信
    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = TENCENT_SMS_APP_ID
    appkey = TENCENT_SMS_APP_KEY
    sms_sign = TENCENT_SMS_SIGN
    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    print(response)
    return response

def send_sms_multi(phone_num_list, template_id, param_list):
    """
    批量发送短信
    :param phone_num_list:手机号列表
    :param template_id:腾讯云短信模板ID
    :param param_list:短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = TENCENT_SMS_APP_ID
    appkey = TENCENT_SMS_APP_KEY
    sms_sign = TENCENT_SMS_SIGN

    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    print(response)
    return response



if __name__ == '__main__':
    code = random.randrange(1000, 9999)
    # send_sms_single(phone_num="13520445436",template_id=842633,template_param_list=[code,])
    send_sms_multi(phone_num_list=["13520445436",'13522488966'],template_id=842633,param_list=[code,])
