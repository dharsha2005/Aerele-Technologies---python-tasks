"""
Method Resolution Order in Python
"""
class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("class B")
class C(A):
    pass
class D(B,C):
    pass
obj = D()
obj.show()
print(D.mro())