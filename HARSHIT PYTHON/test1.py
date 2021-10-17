class person:
    count_instance=0
    def __init__(self,name,surname):
        count_instance=+1
        self.name=name
        self.surname=surname
        
p=person('mani','hi')
p=person('mani','hi')
p=person('mani','hi')

print(person.count_instance)
        