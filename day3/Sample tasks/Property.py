"""
Use of property decorator in python
"""
class Student:
    def __init__(self,add):
        self._name=add
    @property
    def add(self):
        return self._name
    @add.setter
    def add(self,value):
        self._name=value
s1 = Student("Dharshan")
print(s1.add)