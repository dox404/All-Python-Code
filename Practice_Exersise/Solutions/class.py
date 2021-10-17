
f=open('sample.txt')
data=f.read()
print(data)
f.close

class Student:
      
    def __init__(self,Name,village,marks,number):
        self.name=Name
        self.village=village
        self.marks=marks
        self.number=number
        
    def guardian_letter(self):
        print(f"your son is very inteligent sir,i wish a very good future to {self.name}....Thank you")
        
    def phone(self):
        print(f'the phone number of {self.name} is {self.number}')
    def pass_or_fail(self):
        if self.marks<300:
            print('you are failed')
        else:
            print('you are passed')
        
    
    
    
rohan=Student('Rohan','ashua',301,8391019909)
rohan.guardian_letter()
rohan.phone()
rohan.pass_or_fail()

    


    

        
        

        
    
print(data)