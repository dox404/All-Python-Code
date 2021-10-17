def cube_fact(num):
    cube={}
    for i in range(1,num+1):
          cube[i]=i**3
    return cube

print(cube_fact(700))