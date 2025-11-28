class Student:
    def __init__(self,name=None,age=0):
        self.name=name
        self.age=age

obj=Student("hong",20)
obj.age=21
print(obj.age)