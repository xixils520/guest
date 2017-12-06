#   coding=utf-8
import os
import time
from multiprocessing import Process
# f=open(r'C:\mystudy\qiye.txt','w')
# f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'李松')
# f.close()
# print(os.getcwd())
# print('213123s%s' % (time.time()))
def run_proc(name):
    print('第一条线程 %s (%s)...' % (name, os.getpid()))
if __name__=='__main__':
    print('父 %s' % (os.getpid()))
    for i in range(5):
        p=Process(target=run_proc,args=(str(i),))
        print('Process will start')
        p.start()
    p.join()
    print('Process end')

# from multiprocessing import Process
# import os
#
#
# # 子进程代码
# def run_proc(name):
#     print('Run child process %s (%s).' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start..')
#     # 启动子进程
#     p.start()
#     # 等待子进程结束后再继续往下运行
#     p.join()
#     print('Child process end.')