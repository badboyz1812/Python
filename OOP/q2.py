from datetime import date


class Person():
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year,self.dob.month,self.dob.day):
            age -=1
            return age
        

person1 = Person("Pradeep","India",date(2001, 12, 18))

print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.dob)
print("Age:", person1.age())
