sub1=int(input('enter the 1st subject number: '))
sub2=int(input('Enter the 2nd subject number: '))
sub3=int(input('Enter the 3rd subject number: '))
total=sub1+sub2+sub3
p=(total)/3

if p>=40:
    print(f"You are Passed with the persentage of {p}")
else:
    print(f"You are failed with the persentage of {p}")
