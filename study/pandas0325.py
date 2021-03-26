#encoding=utf-8
import pandas as pd ,numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm, rcParams
from eplot import eplot
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

''' eplot使用文档
https://github.com/pjgao/eplot/blob/master/README.md
'''


plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置


data={"subject":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
"score":[1,2,np.nan,4,5,6,7,10]}
df=pd.DataFrame(data)
# print(df,type(df))
# 提取含有特定字符串的行
# solve 1 输出为True的行
# print(df['subject']=='Python')
# print(df[df['subject']=='Python'])
# solve 2
results=df['subject'].str.contains("Python")
# print(results)
results.fillna(value=False,inplace=True)
# print(df[results])

# 3.输出df的所有列名
# print(df.columns)

# 4.修改第二列列名为'popularity'
df.rename(columns={'score':'popularity'},inplace=True)
# print(df)

# 5.统计grammer列中每种编程语言出现的次数
count_num=df['subject'].value_counts()
# print(count_num)

# 6.将空值用上下值的平均值填充
df['popularity']=df['popularity'].fillna(df['popularity'].interpolate())
# print(df)

# 7.提取popularity列中值大于3的行
# print(df[df['popularity']>3])

# 8.按照grammer列进行去除重复值
# print(df.drop_duplicates(['subject']))

# 计算平均值
# print(df['popularity'].mean(),df['popularity'].max())

# print(df.describe())

# 10.将grammer列转换为list
# print(df['subject'].to_list())
# print(df.to_csv('test.csv'))

# print(df.shape)

# print(df[(df['popularity'] > 3) & (df['popularity'] < 7)])
# 交换两列位置
#方法1

# temp = df['popularity']
# df.drop(labels=['popularity'], axis=1,inplace = True)
# df.insert(0, 'popularity', temp)
# print(df)

#方法2
cols = df.columns[[1,0]]
df = df[cols]
# print(df)

# print(df.head(3))
# print(df.tail(5))
# print(df[~df.popularity.isin([8])])
# print(df.drop(index=[7]))
df = df.append({'subject':'Perl','popularity':6.6},ignore_index=True)
# print(df)
pd.set_option('display.width', 1000)#加了这一行那表格的一行就不会分段出现了
# pd.set_option('display.max_colwidth', 1000)
# pd.set_option('display.height', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

# 读取excel文件
data=pd.read_excel('D:/code/study/data/up分区.xlsx')

# print(data)
# print(data.describe())

#分组并指定列名
data1=data.groupby('分区',as_index=False)['up_name'].count()
# print(data1)
#更改列名
# data1.rename(columns={'分区':'spl'},inplace=True)
# print(data1)

#指定索引
data2=data1.set_index('分区')
# print(data2)
#调用pandas的绘图方法
# data2.plot(kind="bar")
# plt.show()

'''
If return type is HTML, you can see the chart directly in jupyter notebook, but cannot change anymore.
If return type is CHART, you need `df.eplot.bar().render_notebook()`  in order to display in notebook.
eplot.set_config(return_type='CHART')
eplot.set_config(return_type='HTML') # default by html
'''

eplot.set_config(return_type='CHART')
data2.eplot.bar().render('d:/code/study/bar26.html')
make_snapshot(snapshot, data2.eplot.bar().render(), "d:/code/study/bar26.png")


