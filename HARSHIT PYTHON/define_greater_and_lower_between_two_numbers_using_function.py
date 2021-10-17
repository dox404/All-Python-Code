def greater_or_lower(a,b):
    if a>b:
        print(f'{a} is greater')
    elif b>a:
        print(f'{b} is greater')
    else:
        print('they are equal')


num1=int(input('enter 1st number: '))
num2=int(input('enter 2nd number: '))
greater_or_lower(num1,num2)
        