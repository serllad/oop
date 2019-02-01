from configparser import ConfigParser
from os import environ
c=ConfigParser()
c.read('area.ini',encoding='utf-8')
l=c.items('messages')
d=dict(l)
print(d)
c.set('numbers','pi','3.14159265358979')
c.write(open('area.ini','w'))
print(environ)
for kv in environ:
    print(kv)