number=[1,2,3,4,5,6,7,8,9,10]
number_for_sq=[2,4,8,16]
numbers_for_cuberoot=[8,9,16,125,216]

cube=list(map(lambda a: a**3, number))
print(f'the cubes are {cube} ')
square =list(map(lambda a: a**2,number))
print(f'the square are {square}')
sq_root=list(map(lambda a: a**1/2,number_for_sq))
print(f'the square roots are {sq_root}')
cube_root=list(map(lambda a: a**1/3,numbers_for_cuberoot))
print(f'the cuberoot are {cube_root}')
