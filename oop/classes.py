class Person:
    #empty class
    pass
class Student:
    name ='Nyagaka'# class attribute
    
    #constructor
    def __init__(self, name, age):
        self.name =name
        self.age =age
        print('Constructor invoked!')
        #instance variables
        self.age =19
         #class methods
    def displayInfo(self):
            print('Personal info: Name: ', self.name ,'Age:' ,self.age)
    @classmethod
    def printWelcome(this):
      print('Welcome' , this.name)
print(Student.name)
details =Student('Vera',19)
print(details.name)
details.displayInfo()
Student.printWelcome()