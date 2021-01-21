## 菜品识别输入代码
```
# encoding:utf-8

import requests
import base64

'''
植物识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
# 二进制方式打开图片文件
f = open(r'D:\api\菜品.jpg', 'rb')
img = base64.b64encode(f.read())
baike_num = 3
params = {"image":img,
          'baike_num':baike_num
         }
access_token = ''
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
```

## 输出代码

