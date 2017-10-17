from time import sleep,ctime

def music():
    print('1music %s'%ctime())
    sleep(2)

def movie():
    print('2movie %s'%ctime())
    sleep(5)

if __name__=='__main__':
    music()
    movie()
    print('all end : %s',ctime())