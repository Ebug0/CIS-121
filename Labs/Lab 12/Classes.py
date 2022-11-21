import Classes

#There are 4 classes that need to be created the first class or the parent class is Addresss whos child is Person and then the person class is the parent class of student and teacher

class address():

    def __init__(self, street, city, country, zipcode, state):
        self.street = street
        self.city = city
        self.country = country
        self.zipcode = zipcode
        self.state = state
    
    def getAddress(self):
        return f"{self.street}, {self.city}, {self.zipcode}, {self.state}, {self.country}"
    
    def getCity(self):
        return self.city

    def getZipcode(self):
        return self.zipcode

    def getState(self):
        return self.state

    def getCountry(self):
        return self.country
    
    def __str__(self):
        return f"Street: {self.street}\nCity: {self.city}\ncountry: {self.country}\nZipcode: {self.zipcode}\nState: {self.state}\n"

class person(address):

    def __init__(self, name, phonenumber, email, street, city, country, zipcode, state):
        super().__init__(street,city,country,zipcode,state)
        self.name = name
        self.phonenumber = phonenumber
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhonenumber: {self.phonenumber}\
        \nEmail: {self.email}\nStreet: {self.street}\nCity: {self.city}\ncountry: {self.country}\nZipcode: {self.zipcode}\nState: {self.state}\n"
    
class student(person):

    def __init__(self, studentnumber, gpa, name, phonenumber, email, street, city, country, zipcode, state):
        super().__init__(name, phonenumber, email, street, city, country, zipcode, state)
        self.studentnumber = studentnumber
        self.gpa = gpa

    def getgpa(self):
        return self.gpa

    def getstudentnumber(self):
        return self.studentnumber

    def __str__(self):
        return f"StudentID: {self.studentnumber}\nGPA: {self.gpa}\nName: {self.name}\nPhonenumber: {self.phonenumber}\
        \nEmail: {self.email}\nStreet: {self.street}\nCity: {self.city}\ncountry: {self.country}\nZipcode: {self.zipcode}\nState: {self.state}\n"
    
class teacher(person):

    def __init__(self, teacherid, workhours, work_rate, years_of_service, name, phonenumber, email, street, city, country, zipcode, state):
        super().__init__(name, phonenumber, email, street, city, country, zipcode, state)
        self.teacherid = teacherid
        self.workhours = workhours
        self.work_rate = work_rate
        self.years_of_service = years_of_service
    
    def getteacherid(self):
        return self.teacherid

    def getworkhours(self):
        return self.workhours

    def getwork_rate(self):
        return self.work_rate

    def getyears_of_service(self):
        return self.years_of_service

    def calculateYearlySalary(self):
        return self.work_rate * self.workhours * 52
    
    def __str__(self):
        return f"TeachID: {self.teacherid}\nHours worked per week: {self.workhours}\nYears of service: {self.years_of_service}\nName: {self.name}\nPhonenumber: {self.phonenumber}\
        \nEmail: {self.email}\nStreet: {self.street}\nCity: {self.city}\nCountry: {self.country}\nZipcode: {self.zipcode}\nState: {self.state}\n"


