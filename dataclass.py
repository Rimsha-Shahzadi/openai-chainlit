# from dataclasses import dataclass
# from typing import ClassVar

# @dataclass
# class American:
#     name: str
#     age: int
#     weight: float
#     language: ClassVar[str] = "English"

#     def speaks(self):
#         return f"{self.name} is speaking... {American.language}"

#     def eats(self):
#         return f"{self.name} is eating..."

#     @staticmethod
#     def country_language():
#         return American.language


# # Call class/static method
# print(American.country_language())

# # Create object
# john = American(name="John", age=23, weight=50)

# print(john.speaks())
# print(john.eats())


# from dataclasses import dataclass
# from typing import TypeVar, 
# @dataclass
# class American:
#     language: ClassVar[str] = "English"
#     national_food: ClassVar[str] = "HumBurger"
#     normal_body_temperature: ClassVar[float] = 98.6
#     name: str
#     age: int
#     weight: float
#     liked_food: str

#     def speaks(self):
#        return f"{self.name} is speaking...{American.language}"
#     def eats(self) :
#        return f"{self.name} is eating..."  

#     @staticmethod
#     def country_language():
#       return American.language
#     #   print(American.country_language())

# john = American(name="John", age= 23,weight=50, liked_food="Pizza")

# print(American.country_language())
# print(john.speaks())
# print(john.eats())
# print(john.name)
# print(john.age)
# print(john.weight)
# print(john)
# print(American.language)


# print(American.country_language())

# from dataclasses import dataclass
# from typing import ClassVar 


# @dataclass
# class Human():
#     name: str
#     age: int

#     def greet(self):
#       return f"Hi, I'm {self.name}"   
#     def works(self):
#       return "I am Working"
#     def __call__ (self):
#        return f"Hello"

# obj1 = Human(name="Rimsha", age=22)
# print(obj1.name)
# print(obj1.age)
# print(obj1.greet())
# print(obj1.works())

# obj1()
# obj1.__dict__


# def greet():
#     return "Hi"
# print(greet)
# from dataclasses import dataclass, field
# from typing import Optional

# @dataclass
# class Person:
#     name: str
#     age: int
#     email: str | None = None
#     tags: list[str] = field(default_factory=list)

#     def is_adult(self) -> bool:
#         """Example method that uses dataclass attributes."""
#         return self.age >= 18

# def demo_good_usage():
#     person1 = Person(name="Alice",age=23, email="alice@example.com")
#     person2 = Person(name="Bob",age=17 )
#     person3 = Person(name="Charlie",age=25, tags=["Student","part-time"])

#     person1.tags.append("Developer")

#     print(f"Person 1: {person1}")
#     print(f"Person 2: {person2}")
#     print(f"Person 3: {person3}")


#     print(f"Is {person1.name} an adult? {person1.is_adult()}")
#     print(f"Is {person2.name} an adult {person2.is_adult()}")
#     print(f"Is {person3.name} an adult? {person3.is_adult()}")

# if __name__ == "__main__":
#     print("===Good Dataclass examples===")
#     demo_good_usage()



# from dataclasses import dataclass, field
# @dataclass
# class Person:
#     name: str
#     age: int
#     email: str | None = None
#     tags: list[str] = field(default_factory=list)

# class PersonBad():
#   def __init__(self, name, age, email=None, tags=None):
#      self.name = name
#      self.age = age
#      self.email = email
#      self.tags = tags if tags is not None else []

#      def __repr__(self):
#         return f"PersonBad(name={self.name}, age={self.age}, email={self.email})"
     
#      def __eq__(self, other):
#         if not isinstance(other, PersonBad):
#            return False
        
#         return (self.name == other.name and
#                 self.age == other.age and
#                 self.email == other.email and
#                 self.tags == other.tags)
# def demo_bad_usage():
#    person1 = PersonBad("Alice", 30, "alice@example.com")
#    person2 = PersonBad("Bob", 25)

#    print(f"PersonBad 1: {person1}")
#    print(f"PersonBad 2: {person2}")

# if __name__ == "__main__":
#   print("===Bad Dataclass examples===")
#   demo_bad_usage()

from dataclasses import dataclass, field
from typing import Callable

@dataclass
class Calculator:
    operation: Callable[[int, int],str]

    def calculate(self, a: int, b: int) -> str:
        return self.operation(a, b)
def add_and_stringify(x: int, y: int) -> str:
    return str(x+y)    
calc= Calculator(operation=add_and_stringify)
print(calc.calculate(13, 7))
