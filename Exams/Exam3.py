

class vehicle():

    def __init__(self, numpassengers, manufacturer, numwheels):
        self.numpassengers = numpassengers
        self.manufacturer = manufacturer
        self.numwheels = numwheels

class automobile (vehicle):

    def __init__(self, mpg, model, numdoors, numpassengers, manufacturer, numwheels):
        super().__init__(numpassengers, manufacturer, numwheels)
        self.mpg = mpg
        self.model = model
        self.numdoors = numdoors

class sedan (automobile):

    def __init__ (self, type, numcylinders, horsepower, mpg, model, numdoors, numpassengers, manufacturer, numwheels):
        super().__init__(mpg, model, numdoors, numpassengers, manufacturer, numwheels)
        self.type = type
        self.numcylinders = numcylinders
        self.horsepower = horsepower
    
class truck (automobile):

    def __init__(self, type, numaxels, maxtowpayload, mpg, model, numdoors, numpassengers, manufacturer, numwheels):
        super().__init__(mpg, model, numdoors, numpassengers, manufacturer, numwheels)
        self.type = type
        self.numaxels = numaxels
        self.maxtowpayload = maxtowpayload

class twowheeler (vehicle):

    def __init__(self, model, weight, numpassengers, manufacturer, numwheels):
        super().__init__(numpassengers, manufacturer, numwheels)
        self.model = model
        self.weight = weight

class motorcycle (twowheeler):

    def __init__(self, type, mpg, horsepower, model, weight, numpassengers, manufacturer, numwheels):
        super().__init__(model, weight, numpassengers, manufacturer, numwheels)
        self.type = type
        self.mpg = mpg
        self.horsepower = horsepower

class bicycle (twowheeler):

    def __init__(self, hasgears, hassuspensions, wheelsize, model, weight, numpassengers, manufacturer, numwheels):
        super().__init__(model, weight, numpassengers, manufacturer, numwheels)
        self.hasgears = hasgears
        self.hassuspensions = hassuspensions
        self.wheelsize = wheelsize
#Question 1 is above
#Questions 2: Vechicle is the parent class of Automobile and TwoWheeler so that mean that Automobile and TwoWheeler will inherant the functions of Vechicle
#Then Sedan and Truck are child classes of Automobile and Motorcycle and Bicycle are child functions of TwoWheeler

#Start of questions 3

class Customer():
    
    def __init__(self):
        self.amount = 0
        self.discountearned = False
    
    def makepurchase (self, amount):
        
        if self.discountearned == True: #if the customer has a discount it is applied to the purchase and gives them 10 dollars off and applys the rest of the purchase to the next discount
            self.amount = amount - 10
            self.discountearned = False
        else:
            self.amount += amount
    
    def discountreached(self):

        if self.amount >= 100: #if the customer has spent 100 dollars they get a discount and their counter goes back by 100
            self.amount -= 100
            self.discountearned = True

def makingpurchase(customer, amount):

    customer.discountreached()  #This checks if the customer spent 100 dollars before the purchase to see if they get a discount
    customer.makepurchase(amount)

if __name__ == "__main__":
    ethan = Customer()

    makingpurchase(ethan, 100)
    makingpurchase(ethan, 95)
    makingpurchase(ethan, 20)
    
    ethan.discountreached()
    print(ethan.amount)
    print(ethan.discountearned)

#I worked with mason snow on this Exam


