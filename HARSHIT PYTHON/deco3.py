def deco(func):
    def inner():
        print('hello')
        func()
        return inner
    
         
def hello():
    print('helo world')
    
    
print(deco(hello()))