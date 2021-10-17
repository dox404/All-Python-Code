#normal way to print 1 to 10 

def numbs(n):
    for i in range(1,n+1):
        yield(i)
    
numbers=list(numbs(10)) #this is a generator object..if i covert it in a list then the loop are 
                    #reapeted what time i will call the loop

        
for i in numbers:
    print(i)
    
for i in numbers:
    print(i)
    
for i in numbers:
    print(i)   
    
for i in numbers:
    print(i)   
    
# how many time i have creating loop it will print one time



