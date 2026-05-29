"""
def cal():
    a=int(input("a: "))
    b=int(input("b: "))
    op=input(" operator: ")
    def add():
        return a+b
    def mul():
        return a*b
    def sub():
        return a-b
    def div():
        return a/b
    def mod():
        return a%b
    if op=='+':
        print(add())
    elif op=='*':
        print(mul())
    elif op=='-':
        print(sub())
    elif op=='/':
        print(div())
    else:
        print(mod())
cal()

""""""
def repeat(x):
    def Dec(func):
        def inner():
            for i in range(x):
                func()
        return inner
    return Dec

@repeat(4)
def greet():
    print("Hello")
greet()

"""
def fun(x):
    def fun2(y):
        def fun3(z):
            y()
        return fun3
    return fun2
k=fun(20)
k(30)

@fun(10)
def greet():
    print("Hiii")
f=fun(greet)
print(f)
