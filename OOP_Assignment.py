class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender =gender
        self.age= age
    def introduce(self):
        print(f'Introducing {person.name}, Gender: {person.gender}, {person.age} years')

person = Person('Nyagaka Vera', 'Female' , 19)
person.introduce()