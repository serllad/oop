from subprocess import Popen,PIPE

with open('exem.html',mode='r') as f:
    buf=f.read()
    tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    tidy.stdin.write(buf.encode())
    tidy.stdin.close()
    print(tidy.stdout.read().decode())