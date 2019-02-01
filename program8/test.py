from xmlrpc.client import *
mypeer=ServerProxy('http://localhost:8886')
code,data=mypeer.query('test.txt')
res=mypeer.hello('http://localhost:8887')
print()