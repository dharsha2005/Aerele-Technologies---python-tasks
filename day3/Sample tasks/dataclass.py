"""
Dataclass in Python
"""

from dataclasses import dataclass
@dataclass
class Student:
    name:str
    age:int
    def details(self):
        return f"{self.name} and {self.age}"
s = Student("Dharshan",21)
print(s.details())