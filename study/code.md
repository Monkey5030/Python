1. 字符串的转义  
```
# v1.0.0及以上
from pymysql.converters import escape_string

# v0.10.1及以下
from pymysql import escape_string


s = r'D:\视频教程\大数据\【开课吧】廖雪峰 · 2019大数据分析\开课吧介绍'
es = escape_string(s)
```
2. logging的简单使用  
```
import logging
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "#配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' #配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    filename=r"D:\code\jupyter-notebook\test.log", #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    filemode='a+'
                    )
logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")
```
