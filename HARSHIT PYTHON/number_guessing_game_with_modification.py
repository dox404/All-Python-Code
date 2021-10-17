winningNumber=45
guess=1
number=int(input("Enter a number 1 to 100: "))
gameOver=False
while not  gameOver:
    if number==winningNumber:
        print(f'you won and you guessed {guess} times')
        gameOver=True
    else:
        if number>winningNumber:
            print('too high')
            number=int(input("Guess again: "))
            guess+=1
        else:
                print('too low')
                number=int(input("Guess again: "))
                guess+=1