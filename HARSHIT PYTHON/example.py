
# #l1=[1,2,3,4]
# #l2=[5,6,7,8]


# def avarage_finder(l1,l2):
#     avg=[]
#     for pair in zip(l1,l2):
#         avg.append(sum(pair)/len(pair))
#     return avg
# a=avarage_finder([1,2,3],[4,5,6])        
# print(a)
        






def avg_finder(**args):
    avg=[]
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg 
    
    
    m=avg_finder([1,2,3],[4,5,6,],[7,8,9])
    print(m)
