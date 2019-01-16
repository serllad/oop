def func(a):
    def infunc():
        nonlocal a
        a=a+1
        return a
    return infunc
it=iter(func(1),4)
print(it)
for i in it:
    print(i)