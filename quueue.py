import threading,queue,time

q=queue.Queue(3)
threads=[]

def worker():
    while True:
        item=q.get()
        if item==None:
            break
        print('i get {}'.format(item))
        time.sleep(1)
        q.task_done()

def produce():
    while True:
        if q.full():
            print('i am full')
        for item in [1, 2, 3, 4, 5, 6, 7, 8]:
            q.put(item)

for i in range(5):
    th=threading.Thread(target=worker)
    th.start()
    threads.append(th)

pth=threading.Thread(target=produce)
pth.start()

q.join()
print('end')
for t in threads:
    t.join()