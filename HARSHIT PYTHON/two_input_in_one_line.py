name,age =input('enter your name and age comma separated: ').split(",")

name.strip()
age.strip()


print(f'your name is {name.strip()}')
print(f'you are {age.strip()} years old')


#erasing the spaces of a string