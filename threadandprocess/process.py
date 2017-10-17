from time import sleep,ctime
import multiprocessing

def super_player(file_,time):
    for i in range(2):
        print('start playing:%s!%s'%(file_,ctime()))
        sleep(time)

lists={'aiqingmaimai.mp3':3,'afanda.mp4':5,'woheni,mp3':4}

threads=[]
files=range(len(lists))

for file_,time in lists.items():
    t=multiprocessing.Process(target=super_player,args=(file_,time))
    threads.append(t)

if __name__=='__main__':
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:%s'%ctime())