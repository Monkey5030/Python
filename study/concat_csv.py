#encoding=utf-8
import pandas as pd
import os
import csv

def concat_csv(filename,dirpath):
    with open(filename,'w') as f:
        cw=csv.writer(f)
        cw.writerow(['name',	'school',	'academy',	'department',	'professional',	'header_img',	'email',	'phone',	'research_direction',	'mainurl',	'content',	'flag'])

    for inputfile in os.listdir(dirpath):
        order=['name',	'school',	'academy',	'department',	'professional',	'header_img',	'email',	'phone',	'research_direction',	'mainurl',	'content',	'flag']
        df=pd.read_csv(dirpath+inputfile,encoding='utf-8-sig')
        try:
            df=df[order]
        except Exception as e:
            print(e,inputfile,df.columns)
        df.to_csv(filename, mode='a', index=False, header=False,encoding='utf-8-sig')
if __name__=='__main__':
    filename='深圳研究生院.csv'
    dirpath='d:/work/202105/数据采集/深圳研究生院/'
    concat_csv(filename,dirpath)
