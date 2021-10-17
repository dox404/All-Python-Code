#iterable-----> where we can use loop again ann again
#example--->list,dicts,sets,tuples
#iterator---->who gives us next element


colors=['red','violet','orange','blue'] #it is a iterable

var=iter(colors) # now it is a itarator object

print(next(var)) # now it is calling iterator obj  one by one...
print(next(var)) #how many time it will called ..it will print the next element
print(next(var))
print(next(var))