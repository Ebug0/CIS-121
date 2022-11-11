from Classes import Car
from Classes import Company
import random

def zeroto60(car):
    count = 0
    while car.speed <= 60:
        acc = random.randint(0,25)
        car.accelerate(acc)
        count += 1
    car.addtime(count)

if __name__ == "__main__":
    car1 = Car(Company("Apple",1), 20, 0, "stopped")
    car2 = Car(Company("Samsung", 2), 150, 0, "stopped")
    car3 = Car(Company("Blackberry",3), 5, 0, "stopped")
    car4 = Car(Company("Xiaomi",4), 50, 0, "stopped")
    carlist = [car1, car2, car3, car4]
    times = {"car1" : 0, "car2":0, "car3": 0, "car4":0}

    for i in carlist:
        zeroto60(i)
    
    for i in carlist:
        i.displayinfo()
    """  
    best = 100000
    fastestcar = None
    for i in carlist:
        if best > i.time:
            best = i.time
            fastestcar = i """
    
