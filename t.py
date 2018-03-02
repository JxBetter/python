def test(func):
    print('start')
    def d(*args,**kwargs):
        print('hi')
        return func(*args,**kwargs)
    return d

@test
def f(s):
    print(s)

f(3)