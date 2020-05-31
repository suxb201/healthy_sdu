import requests
import json

global_session = requests.session()
global_session.headers = {
    "Content-Type": 'application/json'
}

student_id = "*******"

print(global_session.headers)
print(global_session.cookies)
r = global_session.post("https://jkct.sdu.edu.cn/func/wechat/yqsb/miniLogin", data=json.dumps({"code": "****"}))
print('=========================')
print(r)
print(r.text)
print(r.headers)
print(global_session.headers)
print(global_session.cookies['JSESSIONID'])

# preSign
r = global_session.post("https://jkct.sdu.edu.cn/func/wechat/yqsb/preSign", data=json.dumps({"input": student_id}))
print('=========================')
print(r)
print(r.text)

# Sign
r = global_session.post("https://jkct.sdu.edu.cn/func/wechat/yqsb/Sign", data=json.dumps({"input": student_id}))
print('=========================')
print(r)
print(r.text)

r = global_session.post("https://jkct.sdu.edu.cn/func/wechat/yqsb/getNotice", data=json.dumps({"type": "submit"}))
print('=========================')
print(r)
print(r.text)
print(r.headers)
print(global_session.headers)
print(global_session.cookies['JSESSIONID'])

global_headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn",
    "Content-Type": 'application/json'
}

global_cookies = {
    'JSESSIONID': global_session.cookies['JSESSIONID']
}

url = "https://jkct.sdu.edu.cn/func/wechat/yqsb/getNotice"
data = {"type": "submit"}

r = requests.post(url, headers=global_headers, data=json.dumps(data), cookies=global_cookies)
print(r)
print('=========================')
print(r.text)
