sub1=int(input('enter the 1st subject number: '))
sub2=int(input('Enter the 2nd subject number: '))
sub3=int(input('Enter the 3rd subject number: '))
total=sub1+sub2+sub3
p=(total)/3

if sub1<33:
    print('you are failed in subject 1')
else:
    print('you are passed in subject 1')

if sub2<33:
    print('you are failed in subject 2')
else:
    print('you are passed in subject 2')

if sub3<33:
    print('you are failed in subject 3')
else:
    print('you are passed in subject 3')
    
    
if p>40:
    print('you are passed')
else:
    print('you are failed')
    


