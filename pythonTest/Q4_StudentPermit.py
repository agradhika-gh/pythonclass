class Student:
    # _init_ -- is the constructor
    def __init__(self,age):
        self.age = age # here is the age of the student

    def getPermit(self):
        if self.age < 13:
            raise ValueError (f"You are only {self.age} years. Not eligible for permit.")
        else:
            print("You are eligible to get a permit!")


age = int(input("Please enter your age:"))
studentA = Student(age)
try:
    studentA.getPermit()
except ValueError as e:
        print(f"   Error {e}")