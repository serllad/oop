import sys,re
def lines(file):
    for line in file:
        yield line
    yield '\n'
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]

print('<html><head><title>...</title><body>')
title = True
t=[]
with open('demo.txt','r') as f:
    text=f.readline()
    while text:
        t.append(text)
        text=f.readline()
for block in blocks(t):#.+?表示最小匹配
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)#类似str.replace()，对字符串进行正则表达式匹配的替换
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')
