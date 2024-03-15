class Person:
    _id = '1001' #protected
    __ssn = '000' #private
    #empty class pass
    def level(self):
        return 'Freshman'
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
    def level(self):
        return 'Freshman'
print(Student.name)
details =Student('Vera',19)
#Deleting Attribute, Object, Class
#del Student
#del details
#del details.name
print(details.name)
details.displayInfo()
Student.printWelcome()
#single inheritance
class Freshman(Person):
    def info(self):
        welcome = super().level()
        return 'You are a '+welcome
#multiple inheritance
class Sophmore(Student, Person):
    pass
#multilevel inheritance - Grandparent, Parent, Child
#Hierachical inheritance - Parent, two children
freshman =Freshman()
print(freshman.info())
print(issubclass(Freshman, Person))# verify whether it is a subclass