l=[i for i in range(1,8)]
def func(n):
    return n%2==0
#print(func(3))
k=filter(func,l)
for i in k:
    print(i)

