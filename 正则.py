import re
import struct
p=re.compile('^[0-9]{11}@163.com$')
s='13101951590@163.com'
print(re.match(p,s))
s1='It is My Love '
p1=re.compile('[A-Z]+[a-z]*')
print(type(re.search(p1,s1)))
s=re.split(r'[\s+,]','a,b,c d   e')
print(s)
s2=re.compile(r'(A)(\w+)(\1)')
m=re.match(s2,'AxxA')
print(m.group(0),'-',m.group(1),'-',m.group(2),'-',m.group(3))#()括号用来分组，可以用group访问

s3=re.compile(r'[a|,]+\s')
print(re.match(s3,'aaa aal'))
it=re.finditer(s3,'aa, aaa a ')
for i in it:
    print(i)
'''
总结：[]和|的区别和联系
[]和|都表示或
[]只能匹配一位，里面+，×，？等无效
|优先匹配左边的表达式
'''
print('---------------------------------------------------')
p=re.compile(r'a[,\s]\s*')
l=p.findall('a a,a   ')
print(l)
print('----------------------------------------------------')
p = re.compile(r'<a href="(/jobs/\d+)/">(.*?)</a>')
with open('index.html',mode='r') as f:
    bufs=f.read()
    #s=struct.unpack('s',bufs)
    print(p.findall(bufs))

p=re.compile(r'\\{1,}')
s='\ \\ \\\\'
print(re.match(p,s))
