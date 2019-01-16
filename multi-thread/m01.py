import threading
import time
msg_l=[]
format_l=[]
class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)

def talk():
    while True:
        msg=input('>>: ').strip()
        if not msg:continue
        msg_l.append(msg)

def format_msg():
    while True:
        if msg_l:
            res=msg_l.pop()
            format_l.append(res.upper())

def save():
    while True:
        if format_l:
            with open('db.txt','a',encoding='utf-8') as f:
                res=format_l.pop()
                f.write('%s\n' %res)
def main():
    t1 = threading.Thread(target=talk)
    t2 = threading.Thread(target=format_msg)
    t3 = threading.Thread(target=save)
    t1.start()
    t2.start()
    t3.start()
    t=MyThread('MyThread')
    t.start()
    print(threading.enumerate())
if __name__ == '__main__':
    main()
