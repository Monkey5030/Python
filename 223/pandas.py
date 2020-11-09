#coding=utf-8
import pandas as pd ,numpy as np
# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
# pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)#加了这一行那表格的一行就不会分段出现了
# pd.set_option('display.max_colwidth', 1000)
# pd.set_option('display.height', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# sf=pd.DataFrame({'name':['tom','jerry'],
#                  'age':[12,18],
#                  'date':["2020-08-17 19:00:00","2020-09-20 09:00:00"]})
# print(sf.sort_values(by='age',ascending=False))
# # print(sf['name'])
# # print(sf[sf['age']<16])
# # ages=pd.Series([22,35,58],name='age')
# # print(ages)
# dates=pd.date_range('20120101','20200601',periods=6)
# # print(sf.T)
# # df2=pd.DataFrame(np.random.randn(6,4),columns=list('ABCD'))
# # print(df2)
#
# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20201101', periods=6))
# s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
# print(s.str.lower())

# df = pd.DataFrame(np.random.randn(10, 4))
# # print(df)
# # pieces = [df[:3], df[3:7], df[7:]]
# # print(pd.concat(pieces))
# left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
# right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
# print(pd.merge(left,right,how='inner',on='key'))

# df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
#                                              'foo', 'bar', 'foo', 'foo'],
#  'B': ['one', 'one', 'two', 'three',
#  'two', 'two', 'one', 'three'],
#  'C': np.random.randn(8),
#   'D': np.random.randn(8)})
# print(df)
# print(df.groupby(['A','B']).sum())
data=pd.DataFrame({'time':['2020-11-03 12:12','2008-08-08 20:00']})
data['date1']=data['time'].str.replace('-','').str[:7]
data['year']=data['time'].str.replace('-','').str[:4]
data['month']=data['time'].str.replace('-','').str[5:7]
data['hour']=data['time'].str[11:13]
data['minute']=data['time'].str[14:16]
print(data)
