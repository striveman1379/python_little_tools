# -*- coding:utf-8 -*-
import threading
import time
import random
from queue import Queue

# Python的多线程编程与threading模块

'''
python 3中的多进程编程主要依靠threading模块。创建新线程与创建新进程的方法非常类似。threading.Thread方法可以接收两个参数,
第一个是target，一般指向函数名，第二个时args，需要向函数传递的参数。对于创建的新线程，调用start()方法即可让其开始。
我们还可以使用current_thread().name打印出当前线程的名字。 下例中我们使用多线程技术重构之前的计算代码。

'''

'''
def long_time_task(i):
    print("当前子线程：{} - 任务{}".format(threading.current_thread().name, i))
    time.sleep(2)
    print("结果：{}".format(8**20))

if __name__=="__main__":
    start = time.time()
    print("这是主线程：{}".format(threading.current_thread().name))
    t1 = threading.Thread(target=long_time_task,args=(1,))
    t2 = threading.Thread(target=long_time_task,args=(2,))
    t1.start()
    t2.start()

    end = time.time()
    # print("总共用时%s秒"%(end-start))
    print("总共用时{}秒".format(end-start))
'''

'''
这是主线程：MainThread
当前子线程：Thread-1 - 任务1
当前子线程：Thread-2 - 任务2
总共用时0.0009980201721191406秒
结果：1152921504606846976
结果：1152921504606846976
 '''


'''
#如果要实现主线程和子线程的同步，我们必需使用join方法（代码如下所示)
def long_time_task(i):
    print("当前子线程：{} - 任务{}".format(threading.current_thread(),i))
    time.sleep(2)
    print("结果：{}".format(8**20))

if __name__ == '__main__':
    start = time.time()
    print("这是主线程：{}".format(threading.current_thread()))
    thread_list = []
    for i in range(1,3):
        t = threading.Thread(target=long_time_task,args=(i,))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    end = time.time()
    print("总共用时：{}秒".format(end-start))
'''


'''
这时你可以看到主线程在等子线程完成后才答应出总消耗时间(2秒)，比正常顺序执行代码(4秒)还是节省了不少时间

这是主线程：<_MainThread(MainThread, started 19120)>
当前子线程：<Thread(Thread-1, started 17968)> - 任务1
当前子线程：<Thread(Thread-2, started 22240)> - 任务2
结果：1152921504606846976
结果：1152921504606846976
总共用时：2.0015573501586914秒
'''

'''
当我们设置多线程时，主线程会创建多个子线程，在python中，默认情况下主线程和子线程独立运行互不干涉。
如果希望让主线程等待子线程实现线程的同步，我们需要使用join()方法。如果我们希望一个主线程结束时不再执行子线程，我们应该怎么办呢?
我们可以使用t.setDaemon(True)，代码如下所示

使用setDaemon()和守护线程这方面知识有关， 比如在启动线程前设置thread.setDaemon(True)，就是设置该线程为守护线程，
表示该线程是不重要的,进程退出时不需要等待这个线程执行完成。
这样做的意义在于：避免子线程无限死循环，导致退不出程序，也就是避免楼上说的孤儿进程。

thread.setDaemon（）设置为True, 则设为true的话 则主线程执行完毕后会将子线程回收掉,
设置为false,主进程执行结束时不会回收子线程
'''

'''
def long_time_task(i):
    print("当前子线程：{} - 任务{}".format(threading.current_thread(), i))
    time.sleep(2)
    print("结果：{}".format(8**20))


if __name__ == '__main__':
    start = time.time()
    print("这是主线程：{}".format(threading.current_thread()))
    for i in range(5):
        t = threading.Thread(target=long_time_task, args=(i,))
        t.setDaemon(True)
        t.start()
    end = time.time()
    print("总共用时：{}秒".format(end - start))
'''

'''
输出结果：

这是主线程：<_MainThread(MainThread, started 11440)>
当前子线程：<Thread(Thread-1, started daemon 4356)> - 任务0
当前子线程：<Thread(Thread-2, started daemon 20444)> - 任务1
当前子线程：<Thread(Thread-3, started daemon 20432)> - 任务2
当前子线程：<Thread(Thread-4, started daemon 6920)> - 任务3
当前子线程：<Thread(Thread-5, started daemon 19920)> - 任务4
总共用时：0.0009634494781494141秒

从上面结果可以看出，设置setDaemon(True)后，主线程不等子线程运行完毕就结束了（子线程运行时间至少需要2秒）， 故发现总共用时时间很短
'''

# 通过继承Thread类重写run方法创建新进程
'''
除了使用Thread()方法创建新的线程外，我们还可以通过继承Thread类重写run方法创建新的线程，这种方法更灵活。
下例中我们自定义的类为MyThread, 随后我们通过该类的实例化创建了2个子线程。
'''

'''
def long_time_task(i):
    time.sleep(2)
    return 8**20

class MyThread(threading.Thread):
    def __init__(self, func, args, name='',):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        self.result = None

    def run(self):
        print("开始子进程{}".format(self.name))
        self.result = self.func(self.args[0],)
        print("结果：{}".format(self.result))
        print("结束子进程{}".format(self.name))

if __name__=="__main__":
    start = time.time()
    threads = []
    for i in range(1,3):
        t = MyThread(long_time_task,(i,),str(i))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print("总共用时：{}秒".format(end - start))

'''

'''
输出结果：
开始子进程1
开始子进程2
结果：1152921504606846976
结果：1152921504606846976
结束子进程1
结束子进程2
总共用时：2.001917839050293秒
'''


'''
不同线程间的数据共享

一个进程所含的不同线程间共享内存，这就意味着任何一个变量都可以被任何一个线程修改，因此线程之间共享数据最大的危险在于多个线程同时改一个变量，
把内容给改乱了。如果不同线程间有共享的变量，其中一个方法就是在修改前给其上一把锁lock，确保一次只有一个线程能修改它。
threading.lock()方法可以轻易实现对一个共享变量的锁定，修改完后release供其它线程使用。比如下例中账户余额balance是一个共享变量，使用lock可以使其不被改乱
'''

'''
class Account:
    def __init__(self):
        self.balance = 0

    def add(self,lock):
        #获得锁
        lock.acquire()
        for i in range(0,10000):
            self.balance =+ 1
        #释放锁
        lock.release()

    def delete(self,lock):
        # 获得锁
        lock.acquire()
        for i in range(0,10000):
            self.balance = -0
        #释放锁
        lock.release()

if __name__ == '__main__':
    account = Account()
    lock = threading.Lock()
    #创建线程
    thread_add = threading.Thread(target=account.add,args=(lock,),name='Add')
    thread_delete = threading.Thread(target=account.delete,args=(lock,),name='Delete')

    #启动线程
    thread_add.start()
    thread_delete.start()

    #等待线程结束
    thread_add.join()
    thread_delete.join()

    print('The final balance is: {}'.format(account.balance))

'''

# 生产者


class Producer(threading.Thread):
    def __init__(self, name, myqueue):
        threading.Thread.__init__(self, name=name)
        self.queue = myqueue

    def run(self):
        for i in range(1, 5):
            print("{} is producing {} to the queue!".format(self.getName(), i))
            time.sleep(random.randrange(10) / 5)
        print("%s finished!" % self.getName())

# 消费者


class Consumer(threading.Thread):
    def __init__(self, name, myqueue):
        threading.Thread.__init__(self, name=name)
        self.queue = myqueue

    def run(self):
        for i in range(1, 5):
            val = self.queue.get()
            print(
                "{} is consuming {} in the queue.".format(
                    self.getName(), val))
            time.sleep(random.randrange(10))
        print('%s finished!' % self.getName())


def myMain():
    myqueue = Queue()
    producer = Producer("myProducer",myqueue)
    consumer = Consumer("myConsumer",myqueue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('ALL threads finished!')

    if __name__ == '__main__':
        myMain()

'''
队列queue的put方法可以将一个对象obj放入队列中。如果队列已满，此方法将阻塞至队列有空间可用为止。
queue的get方法一次返回队列中的一个成员。如果队列为空，此方法将阻塞至队列中有成员可用为止。
queue同时还自带emtpy(), full()等方法来判断一个队列是否为空或已满，但是这些方法并不可靠，
因为多线程和多进程，在返回结果和使用结果之间，队列中可能添加/删除了成员.

'''
