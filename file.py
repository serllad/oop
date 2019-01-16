with open('read.txt',mode='r') as f:

    strline=f.readline()
    while strline:
        print(strline)
        strline=f.readline()

with open('read.txt', mode='r') as f:

    #seek移动单位是字节

    c=f.read(2)
    while c:
        print(c.replace('\n','l'))
        print(f.tell())
        c=f.read(2)
with open('readme.txt',mode='w') as f:
    f.write('第一行\n第二行\n第三行')
    print(f.tell())
    f.writelines(['第四行','第五行'])