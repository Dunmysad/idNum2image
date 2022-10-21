import idNum2image
import html2img
import pandas as pd
from datetime import datetime

idNums = pd.read_excel(io=r'idNums.xlsx', usecols='A')

def main(idNums, dateTime):
    for i in idNums.to_dict()['身份证号']:
        res = idNum2image.idNum2image(idNums.to_dict()['身份证号'][i])
        if datetime.strptime(dateTime, "%Y-%m-%d") == datetime.strptime(res['samplingTime'].split(' ')[0], "%Y-%m-%d"):
            html2img.html2image(res)
            print(f"{res['name']} {dateTime} √")
        else:
            print(f"{res['name']} {dateTime} x")


if __name__ == '__main__':
    dateTime = input('请输入日期: xxxx-xx-xx\n')
    main(idNums, dateTime)
