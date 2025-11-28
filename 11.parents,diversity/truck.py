class Vehicle:
    def __init__(self,make,model,color,price):
        self.make=make
        self.model=model
        self.color=color
        self.pric=price
    def setMake(self,make):
        self.make=make
    def getMake(self):
        return self.make
    def getDesx(self):
        return "차량 = ("+str(self.make)+","+str(self.model)+","+str(self.color)+","+str(self.price)+")"
class Truck(Vehicle):
    def __init__(self,make,model,color,price,payload):
        super().__init__(make,model, color,price)
        self.payload=payload

    def setPayload(self,payload):
        self.paylod=payload
    def getPayload(self):
        return self.payload

myTruck=Truck("Tesla","Cyber Truck","white",10000,2000)
myTruck.setMake("Tesla")
myTruck.setPayload(2000)
print(myTruck.getDesc())