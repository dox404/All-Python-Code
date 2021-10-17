import pdb
# pdb.set_trace()  
class phone:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
        
    def full_name(self):
        str='the brand name is' +self.name+self.model
        return str
    
 
class Smartphone(phone):
    def __init__(self,name,brand,price,ram,storage,camera):
        super().__init__(name,brand,price)
        self.ram=ram
        self.storage=storage
        self.camera=camera
    def full_details(self):
        str=(f'the phone name is {self.name} and brand name is {self.brand} and price is {self.price}')
        return str
    
# pdb.set_trace()   
class Vsmartphone:
    def __init__(self,name,brand,price,ram,storage,camera,place):
        super().__init__(name,brand,price,ram,storage,camera)
        self.place=place
        
        
p=Vsmartphone('redmi','mi',12000,'8gb','64gb','21mp','india')

print(p.name)