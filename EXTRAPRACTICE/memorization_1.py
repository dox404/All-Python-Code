import time

number=int(input("Enter the number:"))
memory={}
t1=time.time()
def feb(n):
    if n in memory:
        return memory[n]
    if n==1 or n==0:
      value= n
    else:
      value = feb(n-1) + feb(n-2)
      memory[n]=value
    return value


for i in range(31):
   print(i , feb(i))

t2=time.time()

print(f'the time complexity is {t2-t1} ')