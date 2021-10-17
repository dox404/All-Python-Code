class Person:
    def __init__(self,name1,name2,age):
        self.name1=name1
        self.name2=name2
        self.age=age
        
    @classmethod
    def full_name(cls,string):
        name,name2,age= string.split(',')
        return cls(name,name2,age)


    p=Person.full_name('mani,hoque,20')
        