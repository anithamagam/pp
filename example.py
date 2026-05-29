"""
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

"""


def Valid(func):
    def inner():
        user=input("user: ")
        pswd=input("Password: ")
        if user == "anithamagam" and pswd=="1234":
            result=func()
            return result
        else:
            return "Incorrect user or Password"
    return inner

@Valid
def securefile():
    return "Secured File"
f=securefile()
print(f)