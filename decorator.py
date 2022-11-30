'''
def add(a):
    return a+1
def sub(b):
    return b-1
def operator(fun,x):
    t=fun(x)
    return t
print(operator(add,10))
print(operator(sub,10))
'''

'''def add(a):
    return a+1
def sub(b):
    return b-1
def operator(fun,x):
    t=fun(x)
    return t
print(operator(add,10))
print(operator(sub,10))'''

'''def fun():
    def foo():
        print("hello")
    return foo

f=fun()
f()'''

#syntatic decorator
#also called as pi syntax use with @

def outer(fun):
    def foo(x,y):
        if x<y:
            x,y=y,x
        return fun(x,y)
    return foo
@outer
def divide(x,y):
    print(x/y)
divide(4,2)
