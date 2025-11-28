class Student:
    def __init__(self,name=None,age=0):
        self.__name=name
        self.__age=age

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def setName(self,name):
        self.__name=name

    def setAge(self,age):
        self.__age=age

obj=Student("Hong",20)
print(obj.getName())