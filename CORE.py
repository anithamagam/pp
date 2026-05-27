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