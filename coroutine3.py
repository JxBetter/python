def consumer():
    status = True
    while True:
        n = yield status
        if n is None:
            break
        print('我拿到了{}'.format(n))
        if n == 3:
            status = False

    return status


def grouper(result, n):
    while True:
        result[n] = yield from consumer()


def main():
    n = 5
    result = {}
    while n > 0:
        group = grouper(result, n)
        next(group)
        group.send(n)
        group.send(None)
        if result[n] == False:
            print('我只要3,4,5就行啦')
            break
        n = n - 1
    print(result)


if __name__ == '__main__':
    main()
