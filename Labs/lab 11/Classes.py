class Company:
    def __init__ (self, name, id):
        self.name = name
        self.id = id

class Car:
    def __init__(self, company, miles, speed, status):
        self.company = company
        self.miles = miles
        self.speed = speed
        self.status = status
        self.time = 0
    
    def accelerate(self, speed):
        self.speed += speed
        self.status = "moving"
    
    def stop(self):
        self.speed = 0
        self.status = "stop"
    
    def decrease(self, speed):
        self.speed -= speed
        if self.speed <= 0:
            self.speed = 0
            self.status = "stop"
        else:
            self.status = "slowing Down"
    
    def addtime(self,time):
        self.time = time
    
    def displayinfo(self):
        print("=====Car Info======")
        print(f"Company {self.company.name}\nMiles {self.miles}\nSpeed {self.speed}\nStatus {self.status}")
        print(f"0--60 Test {self.time} Seconds")
