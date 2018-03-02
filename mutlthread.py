from threading import Thread,RLock,Condition
from time import sleep

products=[]
lock=RLock()
con=Condition(lock=lock)

class CustomerThread(Thread):
    def run(self):
        while True:
            global products
            con.acquire()
            if 'apple' not in products:
                print('no apple------------i am waiting')
                con.wait()
                print('i have apple')
            products.pop(0)
            con.notify()
            con.release()
            sleep(1)


class ProduceThead(Thread):
    list=['apple','pear','banana']
    i=0
    def run(self):
        while True:
            global products
            con.acquire()
            if len(products)==100:
                con.wait()
            products.append(ProduceThead.list[ProduceThead.i])
            print('i produce {}'.format(ProduceThead.list[ProduceThead.i]))
            ProduceThead.i=ProduceThead.i+1
            if ProduceThead.i==3:
                ProduceThead.i=0
            con.notify()
            con.release()
            sleep(1)

CustomerThread().start()
ProduceThead().start()
