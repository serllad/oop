import time
l=[i for i in range(1,8)]
def func(n):
    return n%2==0
#print(func(3))
k=filter(func,l)
for i in k:
    print(i)


#装饰器
def fun(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return  wrapper
@fun
def hello(*args,**kwargs):
    print(args,kwargs)
hello(19,hobby='lele')
