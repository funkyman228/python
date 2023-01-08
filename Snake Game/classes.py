class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object of the Person class
person = Person("Alice", 25)
person2 = Person("brunt", 85)

# Call the greet method on the object
person.greet()
person2.greet()
print(person2.age)
