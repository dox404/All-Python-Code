# # def group(name,village,id):
# #     full_name=name +' '+ village +' ' + str(id)
# #     print(full_name)
# #     return full_name


# # group('mani','alampur',29)




# # name='      mani       '
# # n=name.strip()
# # print(n)
# # print(len(n))
# # print(n.lower())
# # print(n.upper())
# # print(n.title())
# # print(n.count('m'))
# # print(n)


# # string='The book contains scenes that children can relate to plus each purchase helps save whales.'
# # s=string.replace('children','women')
# # print(s)


# # name='mani'
# # s=name.center(10,'^')
# # print(s)

# # age1=23
# # age2=6
# # if age1 ==23 and age2 ==67:
# #     print('yes1')
# # else:
# #     print("no")
    
# # l=[1,2,3,4,5,'mani',[1,2,3]]

# # if 1 in l:
# #     print('yes')
# # else:
# #     print('no')

# # if l:
# #     print('yes')
# # else:
# #     print('no')



# # i=0
# # while i<=10:
# #     print('yes')
# #     i+=1



# # for i in range(100,0,-5):
  
# #     print(i)


# # def fun(name,age):
# #     n=name+str(age)
# #     print(n)
# #     fun()


# # fun('mani',90)
# a=[1,2,3]
# # b=[]
# # b.extend(a)
# # print(b)

# # a.pop()
# # print(a)
# # name=input('enyter your name: ')
# # namw1='m1ni'
# # if name==namw1:
# #     print('correct')
# # else:
# #     raise TypeError('this is a error from mani')

# # try:
# #     age=int(input('enter your age:'))
# # except ValueError:
# #       print('error')
# # except:
# #     print('invalid input')
# # else:
# #     print('you entered right')
# # finally:
# #     print('this is final ')


# try:
#     a=int(input('enter number 1: '))
#     b=int(input('rnter number 2: '))
# except:
#     print("value error:")
# else:
#     def divide(a,b):
#         div= a/b
#         return div
# finally:
#     print(div)
# import time    
 
# # t1=time.time()      
# num = int(input("Enter a number: "))    
# t1=time.time()
# factorial = 1  
    
# if num < 0:    
#    print(" Factorial does not exist for negative numbers")    
# elif num == 0:    
#    print("The factorial of 0 is 1")    
# else:    
#    for i in range(1,num + 1):    
#        factorial = factorial*i    
#    print("The factorial of",num,"is",factorial)    

# t2=time.time()
# print(t2-t1)
    




# def fectorial(num):
#    factorial = 1  
#    if num < 0:    
#       print(" Factorial does not exist for negative numbers")    
#    elif num == 0:    
#       print("The factorial of 0 is 1")    
#    else:    
#       for i in range(1,num + 1):    
#           factorial = factorial*i    
#       print("The factorial of",num,"is",factorial)
      
#    fectorial(num)
      
      
      
# fectorial(4)

import time

number=int(input("enter a number: "))
t1=time.time()
fectorial=1
for i in range(1,number+1):
       fectorial=fectorial*i
print(f'fectorial of the {number} is {fectorial}')
print(f'{number}X{i}={fectorial}')
t2=time.time()
T=t2-t1
print(f'the time is {T}')