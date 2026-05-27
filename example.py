def Dec(func):
    def inner(x,y):
        func(x*y,x/y)
        print("ending this function")
    return inner
@Dec
def func(a,b):
    print(a,b)
    print(a+b)
func(10,20)