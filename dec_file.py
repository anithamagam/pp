from signal import valid_signals


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



def Dec(func):
    def inner(x,y):
        print("sending integer")
        func(x,y)
    print(f"func:{func}")
    print(f"inner:{inner}")
    return inner
@Dec
def func(a,b):
    #print(a,b)
    print(a+b)
func(10,20)

def Dec(func):
    def inner(x,y):
        if isinstance(x,int) and isinstance(y,int):
            print("Sending Integer")
            func(x,y)
        elif isinstance(x,str) and isinstance(y,str):
            print("Sending Strings")
            func(x,y)
        else:
            print("Invalid Arguments")
    return inner

@Dec
def func(a,b):
    #print(a,b)
    print(a+b)
func(10,20)
func("hello",10)
func("hello","hi")

@Dec
def securefile():
    return "Secured File"
securefile()

def Dec(func):
    def inner():
        user=input("User: ")
        pswd=input("Password: ")
        if user== "anithamagam" and pswd=="1234":
            result=func()
            return result
        else:
            return "Incorrect user name or Password"
    return inner
