import multiprocessing
from time import ctime,sleep
def clock(interval=1):
    while(True):
        print("The time is ",ctime())
        sleep(interval)
if __name__=='__main__':
    p=multiprocessing.Process(target=clock,args=(2,))
    p.start()
