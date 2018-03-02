def coro():
    print('start')
    while True:
        try:
            x = yield 66
        except Exception:
            print('error')
        else:
            print('x=', x)


def pro(c):
    for i in range(10):
        yield c.send(i)


c = coro()
next(c)
p = pro(c)

for j in p:
    print(j)
c.throw(StopIteration)
