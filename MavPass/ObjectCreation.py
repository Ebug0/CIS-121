class person:
    def __init__(self, age, gender, occupation):
        self.age = age
        self.gender = gender
        self.occupation = occupation
    
    def __str__(self):
        print(f"My {self.gender}, i'm {self.gender} and I work as a {self.occupation}")

    def agecompare(self, person2):
        if self.age > person2.age:
            print("I'm the older one")
        else:
            print("The second person is older")

Burger = person(19, "male", "College student")
Mado = person(17, "Male", "Interesting")

Burger.agecompare(Mado)


