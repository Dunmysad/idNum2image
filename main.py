import idNum2image
import pandas as pd

idNums = pd.read_excel(io=r'idNums.xlsx', usecols='A')

for i in idNums.to_dict()['身份证号']:
    idNum2image.idNum2image(idNums.to_dict()['身份证号'][i])