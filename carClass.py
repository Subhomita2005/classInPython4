class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.model= model
        self.color= color
        self.company= company
        self.speedLimit= speedLimit
        
    def start(self):
        print("Start")
    def stop(self):
        print("Stop")
    def changeGear(self,gearType):
        print("Change Gear")
audi = Car("A6","Red","Audi","80")
print(audi.color) 
audi.start()                  