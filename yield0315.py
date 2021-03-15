#生成器
def yield_test():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

from itertools import islice
print(list(islice(yield_test(),26)))
print(isinstance("中国",str))

#++i +=1
i=0
j=0
while i<=10:
    i=i+1
    j=++j
    print(i,j)


#字符串拼接
strlist=['1','2','3']
print('.'.join(strlist))

#统计字符串在列表中出现的次数
some_data=["a","2",2,4,5,"2","b",4,7,"a",5,"d","a","z"]
count_frq=dict()
for item in some_data:
    if item in count_frq:
        count_frq[item]+=1
    else:
        count_frq[item]=1
print(count_frq)

from collections import defaultdict
count_frq1=defaultdict(int)
for item in some_data:
    count_frq1[item]+=1

print(count_frq1)


count_set=set(some_data)
coout_list=[]
for item in count_set:
    coout_list.append((item,some_data.count(item)))

print(dict(coout_list))

#引入Counter模块
from collections import Counter
a1=Counter(some_data)
print("计数：",a1.most_common())