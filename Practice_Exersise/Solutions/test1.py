# a=int(input('enter the first number: '))
# b=int(input('enter the 2nd number: '))
# # a=a+b
# # b=a-b
# # a=a-b
# c=a
# a=b
# b=c

# print('the value of a:', a)
# print('the value of b: ', b)

# year=2016
# if (year%4)==0:
#     if (year%100)==0:
#         if(year%400)==0:
#              print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")






def leapyear(year):
    if (year%4)==0:
        if (year%100)==0:
            if (year%400)==0:
                return True
            else:
                return 0
        else:
            return True
    else:
        return 0



m=leapyear(2016)
print(m)