class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        
    def full_name(self):
        ful= self.fname +' '+ self.lname
        return ful
    
    def is_avobe(self):
        if self.age>18:
            return True
        
        
        
p=Person('mani','hoque',20)
print(p.fname)
print(p.full_name())
print(p.is_avobe())