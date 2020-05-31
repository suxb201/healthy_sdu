import requests
import json

# url = 'https://jkct.sdu.edu.cn/func/wechat/yqsb/getNotice'
# url = 'https://jkct.sdu.edu.cn/func/wechat/yqsb/miniLogin'

global_headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn",
    "Content-Type": 'application/json'
}

global_cookies = {
    'JSESSIONID': '***********************************************************',
    'Path': '/',
    'HttpOnly': ''
}

def post_info():
    url = "http://jkct.sdu.edu.cn/func/wechat/yqsb/submit"
    data = {
        "curChange": "",
        "isEnglish": False,
        "onsubmit": True,
        "s_selectQdTemperatureTime": False,
        "s_fk": False,
        "s_selectAddressType": False,
        "s_selectDateBack": False,
        "s_Selecttype_backOrAway": False,
        "nowDate": "2020-05-20 22:06",
        "qdTemperature": "36.5",
        "qdTemperatureTime": "01:01",
        "state_fever_user": False,
        "state_fever_family": False,
        "state_condition": False,
        "conditionList": [],
        "input_condition": "",
        "type_fk": "否",
        "state_jzyxgc": False,
        "typeOfjzyxgc": "",
        "state_jjyxgc": False,
        "typeOfjjyxgc": "",
        "state_inhome": True,
        "address": "************************************************地址",
        "qd_state_village_pest": False,
        "qd_state_viapest": False,
        "qd_state_contactpest": False,
        "qd_state_contacthbpest": False,
        "qd_state_contactpest_family": False,
        "typeOfpromise": True,
        "userType": "bks",
        "state_contactpest": False,
        "ex_case": "否",
        "ex_case_contact": "否",
        "ex_case_neighbor": "否",
        "ex_fourteen_back": "否",
        "ex_fourteen_fever": "否",
        "ex_pest_contact": "否",
        "ex_test": "否",
        "condition": "无症状",
    }
    r = requests.post(url, headers=global_headers, data=json.dumps(data), cookies=global_cookies)
    print(r)
    print('=========================')
    print(r.text)


post_info()
