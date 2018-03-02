def coro():
    print('start')
    while True:
        x = yield
        if x is None:
            break
    print('end')
    return 66

def grouper(result,i):
    while True:
        result[i] = yield from coro()

def main():
    result={}
    for i in range(10):
        group=grouper(result,i)
        next(group)
        group.send(i)
        group.send(None)

    print(result)

if __name__ == '__main__':
    main()
