winning_number=55
number_input=int(input("Enter your number: "))
if number_input==winning_number:
    print('you won')
else:
    if number_input>winning_number:
        print("you guassed greater")
    else:
        print('you guassed lower than the winning number')

