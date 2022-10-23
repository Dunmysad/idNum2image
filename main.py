from datetime import datetime
import idNum2image
import html2img
import pandas as pd

idNums = pd.read_excel(io=r'idNums.xlsx', usecols='A')

def main(idNums, dateTime):
    if dateTime:
        pass
    else:
        dateTime = datetime.strftime(datetime.today(), '%Y-%m-%d')
    for i in idNums.to_dict()['身份证号']:
        idNum = idNums.to_dict()['身份证号'][i]
        jsondata_all = idNum2image.idNum2image(idNum)
        # print(type(jsondata_all['data']), jsondata_all['data'])
        if jsondata_all['data']:
            pass
        else:    
            print(idNum, '未查询到数据')
        for i in range(len(jsondata_all['data'])):
            if jsondata_all['data'][i]['samplingTime'].split(' ')[0] == dateTime:
                res = jsondata_all['data'][i]
                html2img.html2image(res)
                print(jsondata_all['data'][i]['name'], jsondata_all['data'][i]['samplingTime'].split(' ')[0], '√')
                break
            else:
                try:
                    print(jsondata_all['data'][0]['name'], dateTime, 'x')
                except Exception as e:
                    print(e)
                finally:
                    break


    
if __name__ == '__main__':
    dateTime = input('请输入日期: (格式: xxxx-xx-xx 回车为当天日期)\n')
    main(idNums, dateTime)
