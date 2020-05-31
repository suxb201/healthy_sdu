import requests
import json

# url = 'https://jkct.sdu.edu.cn/func/wechat/yqsb/getNotice'
# url = 'https://jkct.sdu.edu.cn/func/wechat/yqsb/miniLogin'

global_headers = {
    "Content-Type": 'application/json'
}

global_cookies = {
    'JSESSIONID': '*****'
}

r = requests.post("https://jkct.sdu.edu.cn/func/wechat/yqsb/getNotice", headers=global_headers, data=json.dumps({"type": "submit"}), cookies=global_cookies)
print(r, r.text)
