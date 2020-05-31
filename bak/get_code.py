import requests
import json

global_headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn",
    "Content-Type": 'application/json'
}

global_cookies = {
    'JSESSIONID': '******'
}

url = "https://servicewechat.com/wxa-dev-logic/jslogin?_r=0.5017947553947279&newticket=Ut8cKsaT7CVs_g0Q4-N5araal0h_E-HjGSmLW8ltPC0&appid=wx4dd641aaf8f42f3f&platform=0&ext_appid=&os=win&clientversion=1021905151&os=win&clientversion=1.02.1905151&osversion=6.1.7601"
data = {"scope": ["snsapi_base"]}

r = requests.post(url, headers=global_headers, data=json.dumps(data), cookies=global_cookies)
print(r)
print('=========================')
print(r.text)
