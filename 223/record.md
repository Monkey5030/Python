# 编码设置  
UnicodeEncodeError:'gbk' codec can't encode character '\xa9' in position 0:illegal multibyte sequence  
问题：python的print()方法的问题。在python中， print()方法在Win7的默认编码是gbk，它在打印时，并不是所有的字符都支持的。 而且这个问题一般也就是在cmd中才会有。 在cmd中是改变标准输出编码： 修改准输出编码  
```
import io  
import sys 
#改变标准输出的默认编码 
#utf-8中文乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
```


字符串格式化显示
map() ,reduce() ,filter() 列表表达式
map函数仅仅是创建一个待运行的命令容器，只有其他函数调用它的时候才返回结果。
在常见的数据挖掘工作中，脏数据包括如下内容。
·缺失值。
·异常值。
·不一致的值。
·重复数据及含有特殊符号（如#、￥、*）的数据
从总体上来说，缺失值的处理分为删除存在缺失值的记录、对可能值进行插补和不处理3种情况

python字符串反转
https://www.cnblogs.com/taceywong/p/8045127.html
第一种：使用字符串切片
result = s[::-1]
第二种：使用列表的reverse方法
l = list(s)
l.reverse()
result = "".join(l)
第三种：使用reduce
result = reduce(lambda x,y:y+x,s)
第四种：使用递归函数
def func(s):
    if len(s) <1:
        return s
    return func(s[1:])+s[0]
result = func(s)
第五种：使用栈
def func(s):
    l = list(s) #模拟全部入栈
    result = ""
    while len(l)>0:
        result += l.pop() #模拟出栈
    return result
result = func(s)
第六种：for循环
def func(s):
    result = ""
    max_index = len(s)-1
    for index,value in enumerate(s):
        result += s[max_index-index]
    return result
result = func(s)

类型在pandas中转换
https://www.cnblogs.com/onemorepoint/p/9404753.html

在pandas中取消科学计数法打印
pd.set_option('display.float_format', lambda x: '%.f' % x)
