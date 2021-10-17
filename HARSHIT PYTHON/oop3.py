class laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        
    def apply_discount(self,dis_persentage):
          discount=(dis_persentage/100)*self.price
          return discount

p=laptop('lenovo',"ideapad gaming",63000)
print(p.apply_discount(50))