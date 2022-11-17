class Dog:
    def __init__(self, color, eyecolor, height, length, weight):
        self.color = color
        self.eyecolor = eyecolor
        self.height = height
        self.length = length
        self.weight = weight
        self.status = ""
    
    def sit(self):
        print("I'm sitting!")
        self.status = "I'm sitting!"
    
    def Lay_Down(self):
        print("I'm laying down!")
        self.stauts = "I'm laying down!"


class Person:
    def __init__(self, name, age, lastname):
        self.name = name
        self.age = age
        self.lastname = lastname

    def display(self):
        print(self.name)
        print(self.age)
        print(self.lastname)
    
    def AgeChange(self, age):
        self.age = age

class Employee:
    def __init__(self, name, paidperhour, hoursperweek, position):
        self.name = name
        self.paidperhour = paidperhour
        self.hoursperweek = hoursperweek
        self.position = position
    
    def yearlypay(self):
        print(f"{self.name} yearly pay is ${(self.paidperhour * self.hoursperweek)*52}")

import random
class Student:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        self.__ssn = random.randint(100000000,999999999)
        
    def displayinfo(self):
        print(f"Name: {self.name}")
        print(f"Lastname: {self.lastname}")
        print(f"SNN: {self.__snn}")

class HighSchoolStudent(Student):
    def __init__(self,name, lastname, grade):
        super().__init__(name,lastname)
        self.grade = grade

class Client:
    def __inti__(self, username, password, recoverypass):
        self.__username = username
        self.__password = password
        self.recoverypass = recoverypass
    
    def usernamechange (self, username, password):
        if self.username == username and self.password == password:
            newusername = input("Please enter in the new username")
            self.__username = newusername
        else:
            print("Your username or password was incorrect please try again")
        
    def usernamechange (self, username, password):
        if self.username == username and self.password == password:
            newpassword = input("Please enter in the new password")
            self.__password = newpassword
        else:
            print("Your username or password was incorrect please try again")

class Document:

    def __init__(self,authors,date):
        self.author = authors
        self.date = date

    def getAuthors(self):
        return self.author

    def addAuthors(self,name):
        self.author.append(name)

        if name in self.author:
            print(f"Name: {name} added to the list of authors!")
        else:
            print("Some error occured and the name was not added")
        
           
