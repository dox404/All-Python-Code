import time
t1=time.time()
def evan(a):
    for i in range(1,a+1):
        if i%2==0:
            print(i)
            
evan(20)           
# g=(evan(20))

# for num in g:
#     print(num)

    
# for num in g:
#     print(num)

# for num in g:
#     print(num)
    
t2=time.time()
print(t2-t1)
