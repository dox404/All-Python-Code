#MADHYAMIK GRADE CALCULATOR

sub1=int(input('enter the mars ins Bengali: ',))
sub2=int(input('enter the mars ins English: '))
sub3=int(input('enter the mars ins Math: '))
sub4=int(input('enter the mars ins P.science: '))
sub5=int(input('enter the mars ins L.science: '))
sub6=int(input('enter the mars ins History: '))
sub7=int(input('enter the mars ins Geography: '))

total=(sub1+sub2+sub3+sub4+sub5+sub6+sub7)
persentage=total/7

print(f"your total marks is {total}")

if persentage>=90:
    print('your overall Grade is AA')
elif 80<=persentage<89:
    print('your overall Grade is A+')
elif 60<=persentage<=79:
    print('your overall Grade is A')
elif 45<=persentage<=59:
    print('your overall Grade is B+')
elif 35<=persentage<=44:
    print('your overall Grade is B')
elif 25<=persentage<=34:
    print('your overall Grade is C')
else:
    print('You are disqualified')
    