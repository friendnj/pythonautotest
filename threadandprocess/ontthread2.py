from time import sleep,ctime
import threading

def music(func,loop):
    for i in range(loop):
        print('11111music11111%s %s'%(func,ctime()))
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print('22222movie22222%s %s'%(func,ctime()))
        sleep(5)

threads=[]
t1=threading.Thread(target=music,args=('AAA',2))
threads.append(t1)

t2=threading.Thread(target=movie,args=('BBB',2))
threads.append(t2)


if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all end : %s', ctime())