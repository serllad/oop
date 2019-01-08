import sys
from pkg01 import *
print(type(sys.path))
for item in sys.path:#打印包的系统搜索路径
    print(item)
