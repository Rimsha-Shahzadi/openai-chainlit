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

from dataclasses import dataclass
from typing import ClassVar 


@dataclass
class Human():
    name: str
    age: int

    def greet(self):
      return f"Hi, I'm {self.name}"   
    def works(self):
      return "I am Working"
    def __call__ (self):
       return f"Hello"

obj1 = Human(name="Rimsha", age=22)
print(obj1.name)
print(obj1.age)
print(obj1.greet())
print(obj1.works())

obj1()
obj1.__dict__


# def greet():
#     return "Hi"
# print(greet)