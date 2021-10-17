Text=input('Enter your text: ')

index=len(Text)

if index<10:
    print(f'The text contains less than 10 characters and its number is {index}')
elif index==10:
    print('The Text contains 10 Characters')
else:
    print(f'The text contains more than 10 character and its number is {index} ')
