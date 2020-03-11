 -*- coding:utf-8 -*-
import os
import time,random
from multiprocessing import Process,Pool,cpu_count,Queue



# 多进程multiprocessing
# Process([group [, target [, name [, args [, kwargs]]]]])
# target表示调用方法的名字
# args表示被target的位置参数元组
# kwargs表示target的字典
# name是别名
# group分组

'''
#单进程计算
def long_time_task():
    print("当前进程：{}".format(os.getpid()))
    time.sleep(2)
    print("计算结果:{}".format(8**20))

if __name__ == '__main__':
    print("当前父进程：{}".format(os.getpid()))
    start = time.time()
    for i in range(2):  #让其重复计算两次，与下面创建两个新的进程做对比
        long_time_task()

    end = time.time()
    print("用时{}秒".format(end-start))
'''

'''
程序输出：

当前父进程：14764
当前进程：14764
计算结果:1152921504606846976
当前进程：14764
计算结果:1152921504606846976
用时4.00053071975708秒
'''




'''
#多进程计算

def long_time_task(i):
    print("子进程：{} - 任务{}".format(os.getpid(),i))
    time.sleep(2)
    print("结果：{}".format(8**20))

if __name__ == '__main__':
    print("当前母进程：{}".format(os.getpid()))
    start = time.time()
    p1 = Process(target=long_time_task,args=(1,))
    p2 = Process(target=long_time_task,args=(2,))
    print("等待所有子进程完成。。")
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()
    print("用时{}秒".format(end-start))
'''

'''
程序输出：

当前母进程：3712
等待所有子进程完成。。
子进程：2640 - 任务1
子进程：7308 - 任务2
结果：1152921504606846976
结果：1152921504606846976
用时2.346952438354492秒


我们利用multiprocess模块的Process方法创建了两个新的进程p1和p2来进行并行计算。Process方法接收两个参数, 
第一个是target（target 是由 run() 方法调用的可调用对象。它默认为 None ，意味着什么都没有被调用。），一般指向函数名，
第二个时args（args 是目标调用的参数元组。 kwargs 是目标调用的关键字参数字典。），需要向函数传递的参数。
对于创建的新进程，调用start()方法即可让其开始。我们可以使用os.getpid()打印出当前进程的名字。

输出结果如下所示，耗时变为2秒，时间减了一半，可见并发执行的时间明显比顺序执行要快很多。你还可以看到尽管我们只创建了两个进程，
可实际运行中却包含里1个母进程和2个子进程。之所以我们使用join()方法就是为了让母进程阻塞，等待子进程都完成后才打印出总共耗时，否则输出时间只是母进程执行的时间。

'''

'''
#使用进程池

def long_time_task(i):
    print("子进程：{} - 任务{}".format(os.getpid(),i))
    time.sleep(2)
    print("结果：{}".format(8**20))

if __name__=="__main__":
    print("CPU内核书：{}".format(cpu_count()))
    print("当前母进程：{}".format(os.getpid()))
    start =time.time()
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print("等待所有子进程完成")
    p.close()
    p.join()
    end = time.time()
    print("总共用时: {}秒".format(end-start))
    
'''

'''
输出结果：

CPU内核书：8
当前母进程：18584
等待所有子进程完成
子进程：3584 - 任务0
子进程：1536 - 任务1
子进程：11356 - 任务2
子进程：15772 - 任务3
结果：1152921504606846976
子进程：3584 - 任务4
结果：1152921504606846976
结果：1152921504606846976
结果：1152921504606846976
结果：1152921504606846976
总共用时: 4.563611030578613秒


ps:
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()或terminate()方法，让其不再接受新的Process了。
上面程序进行了5个任务，进程池中有4个进程，每个进程花费时间为2s，前四个任务都执行完毕后，第五个任务再分配给进程池中的其中一个进程，
所以耗费时间总共为4,56秒
'''



#多进程间的数据共享与通信

'''
通常，进程之间是相互独立的，每个进程都有独立的内存。通过共享内存(nmap模块)，进程之间可以共享对象，
使多个进程可以访问同一个变量(地址相同，变量名可能不同)。多进程共享资源必然会导致进程间相互竞争，
所以应该尽最大可能防止使用共享状态。还有一种方式就是使用队列queue来实现不同进程间的通信或数据共享，这一点和多线程编程类似。

下例这段代码中中创建了2个独立进程，一个负责写(pw), 一个负责读(pr), 实现了共享一个队列queue
'''

'''
#写数据，进程执行的代码
def write(q):
    print("process to write: {}".format(os.getpid()))
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

#读数据，进程执行的代码
def read(q):
    print("Process to read:{}".format(os.getpid()))
    while True:
        value = q.get()
        print('Get %s from queue.'%value)


if __name__=="__main__":
    #父进程创建queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程pw,写入：
    pw.start()
    #启动子进程pr，读取：
    pr.start()
    #等待pw结束：
    pw.join()
    #pr进程里是死循环，无法等待其结束，只能强行终止：
    pr.terminate()
'''

'''
输出结果：

process to write: 6080
Put A to queue...
Process to read:8068
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
'''

