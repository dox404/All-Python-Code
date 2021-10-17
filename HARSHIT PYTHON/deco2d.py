
def deco1(func):
    def innter1():
        print('hola')
        func()
    return innter1

def deco0(fun):
    def inter0():
        print("hi")
        fun()
    return deco0

    
@deco0
def main_func():
    print('hello')

main_func()