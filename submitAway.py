import requests
import json
import schedule
import time
import random
import fire


def job(jsessionid):
    data = {
        "isEnglish": False,
        "statePromise": True,
        "onsubmit": True,
        "temperatureM": "36.4",
        "temperatureN": "36.3"
    }
    r = requests.post(
        "https://jkct.sdu.edu.cn/func/wechat/yqsb/submitAway",
        headers={"Content-Type": 'application/json'},
        data=json.dumps(data),
        cookies={'JSESSIONID': jsessionid}
    )
    print(r, r.text)


def run(jsessionid):
    schedule.every().day.at("8:00").do(job, jsessionid)
    schedule.every().day.at("14:00").do(job, jsessionid)
    schedule.every().day.at("20:00").do(job, jsessionid)

    while True:
        schedule.run_pending()
        time.sleep(random.randint(0, 7200))


fire.Fire()
