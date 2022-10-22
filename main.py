import idNum2image
import html2img
import pandas as pd

idNums = pd.read_excel(io=r'idNums.xlsx', usecols='A')

def main(idNums, dateTime):
    for i in idNums.to_dict()['身份证号']:
        jsondata_all = idNum2image.idNum2image(idNums.to_dict()['身份证号'][i])
        # print(type(jsondata_all['data']), jsondata_all['data'])
        for i in range(len(jsondata_all['data'])):
            if jsondata_all['data'][i]['samplingTime'].split(' ')[0] == dateTime:
                res = jsondata_all['data'][i]
                html2img.html2image(res)
                print(jsondata_all['data'][i]['name'], jsondata_all['data'][i]['samplingTime'].split(' ')[0], '√')

                
if __name__ == '__main__':
    dateTime = input('请输入日期: xxxx-xx-xx\n')
    main(idNums, dateTime)
