# year=int(input("Enter year: "))




# # 4 , 100 !=0 => leap
# # 1.

# # if (year%4)==0:
# #     if (year%100)==0:
# #         if(year%400)==0:
# #              print(f"{year} is a leap year")
# #         else:
# #             print(f"{year} is not a leap year")
# #     else:
# #         print(f"{year} is a leap year")
# # else:
# #     print(f"{year} is not a leap year")

# # def leap_year()
# # fibonacci series
# # 0 1 1 2 3 5 8 13 21 ... n => 10
# # start => 2,
# # next: 3,
# # sum => star + next 

# # a = 30
# # b = 50

# # a = a+b-a




def leapYear(year):

    if (year%4)==0:
        if (year%100)==0:
            if(year%400)==0:
                 print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
            
            

m= leapYear(2016)
print(m)
   
   

            
            
            
        