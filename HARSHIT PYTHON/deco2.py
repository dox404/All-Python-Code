def func1(func):
    print('hello wolrd 1')
    return func()


@func1    
def func2():
    print('hello world 2')
    
  
func2()

    