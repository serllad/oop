class myexception(ZeroDivisionError):
    pass
def func(n):
    if n<0:
        raise myexception
try:
    func(0)
except myexception as e:
    print('烦死了')