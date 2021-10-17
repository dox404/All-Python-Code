# # def deco(fun):
# #     def inner():
# #         print('hi i am mani')
# #         fun()
# #     return inner


# # @deco
# # def func():
# #     print('i am from alampur')

# # func()
# from functools import wraps

# def print_function_data(fun):
#     @wraps(fun)
#     def inner(**args,*kwargs):
#         print(f'you are calling{fun} function')
#         return fun(*args,**kwargs)
#     return inner

# @print_function_data
# def add(a,b):
#     return a+b

# add(2,4)
