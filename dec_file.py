def Dec(func):
    def inner(x,y):
        print("starting this function")
        func(x,y)
    print(f"func:{func}")
    print(f"inner:{inner}")
    return inner
@Dec
def func(a,b):
    print(a,b)
    print(a+b)
    print(f"func:{func}")
func(10,20)