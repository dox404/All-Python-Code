number=int(input("Enter the number: "))

if (number%1)==0:
    if (number%number)==0:
         print('number is prime')
    else:
         print('number is not prime')
else:
    print("number is not prime")