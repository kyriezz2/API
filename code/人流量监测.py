
import requests
import base64

'''
人流量统计
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"
# 二进制方式打开图片文件
f = open('human.jpg', 'rb')  #上传人流量图像
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '[此处输入你获取到的token]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
	
	'''
	输出
	{'person_num': 14, 'log_id': 8386600918089470214}  #识别图像中的人流量数字结果
	'''