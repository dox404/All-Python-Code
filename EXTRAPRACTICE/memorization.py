import time

number=int(input("Enter the number:"))

t1=time.time()
def feb(n):
   if n==1 or n==0:
      return n
   else:
      return feb(n-1)+feb(n-2)


for i in range(number+1):
   print(i , feb(i))

t2=time.time()

print(f'the time complexity is{t2-t1} ')







