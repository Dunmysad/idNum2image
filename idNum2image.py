import requests
import re

resType = {0: '阴性'}
r = re.compile('[\u4e00-\u9fa5]+')

def idNum2image(idNum):
    url = 'https://xxapp-api.ziyunzhihui.com/app-server/nucleicAcidResult/findResultEs'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36'
    }

    proxies = {
        "http": None,
        "https": None,
    }

    data = {
        'idNum': idNum
    }

    try:
        res = requests.post(url, headers=headers, data=data, proxies=proxies).json()['data'][0]
        # print(res['name'], res['idNum'], res['samplingTime'], res['reportDate'], res['sampleNumber'], r.findall(res['detectionMechanism'])[0], resType[res['resultType']])
        return res
    except Exception as e:
        print(e)

    
   
