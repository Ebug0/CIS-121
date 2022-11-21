from Classes import *

#There are 4 classes that need to be created the first class or the parent class is Addresss whos child is Person and then the person class is the parent class of student and teacher


if __name__ == "__main__":
    Address = address("165 sickamore street", "Waconia", "United States", 54678, "MN")
    Person = person("Bob", "952-546-858", "BobM@teacher.org", "165 sickamore street", "Waconia", "United States", 54678, "MN")
    Bob = teacher(156475, 40, 35.67, 10, "Bob", "952-546-858", "BobM@teacher.org", "165 sickamore street", "Waconia", "United States", 54678, "MN")
    Joe = student(68746, 4.0, "Joe", "952-546-850", "JoeM@student.org", "160 sickamore street", "Waconia", "United States", 54678, "MN")

    print(Address)
    print(Person)
    print(Bob)
    print(Joe)
