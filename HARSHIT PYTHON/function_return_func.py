# def anu_func():
#     def statement():
#         print('hello world')
#     return statement


# var= anu_func()
# var()



def power(x):
    def to_power(y):
        return y**x
            
    return to_power



var=power(2)
print(var(7))









