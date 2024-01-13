'''
Reference: https://www.geeksforgeeks.org/encapsulation-in-python/
'''

# Creating a base class 
class Base: 
    def __init__(self): 
        # Public member
        self.c = 4
        # Protected member
        self._a = 2
        # Private member
        self.__b = 3

# Creating a derived class 
class Derived1(Base): 
    def __init__(self): 
        # Calling constructor of Base class 
        super().__init__() 
        print("Calling protected member of base class:", self._a) 
        # Modify the protected variable: 
        self._a = 7
        # Protected member
        self._d = 11
        self._e = 77
        # Attempting to access private member (won't work)
        # Uncommenting the following line will result in an AttributeError
        # print("Trying to access private member inside child class:", self.__b)


# Creating another derived class
class Derived2(Base):
    def __init__(self):
        super().__init__()
        self._a = 8
        self._d = 22
        self._e = 66

# Creating a class inheriting from multiple derived classes
class leafClass1(Derived1, Derived2):
    def __init__(self):
        super().__init__()

# Creating another class with a different order of inheritance
class leafClass2(Derived2, Derived1):
    def __init__(self):
        super().__init__()
        # Setting _e from Derived1 instead of Derived2
        self._e = Derived1()._e


# Creating instances
obj1 = Base()   
obj2 = Derived1() 
obj3 = Derived2()
obj4 = leafClass1()
obj5 = leafClass2()

# Accessing public member
print("obj1.c:", obj1.c)  # Output: 4
print("obj2.c:", obj2.c)  # Output: 4

# Accessing protected members
print("Accessing protected member of obj1:", obj1._a)  # Output: 2
print("Accessing protected member of obj2:", obj2._a)  # Output: 2
print("Accessing protected member of obj3:", obj3._a)  # Output: 2
print("Accessing protected member of obj3:", obj3._d)  # Output: 22 (modified in Derived2)
print("Accessing protected member of obj4:", obj4._d)  # Output: 11 (modified in Derived1)
print("Accessing protected member of obj5:", obj5._d)  # Output: 22 (modified in Derived2)

# Accessing protected member _e of obj5 using the new method
print("Accessing protected member _e of obj5:", obj5._e)

# Accessing private members
print("Accessing private member of obj2:", obj2._Base__b)  # Output: 3
print("Accessing private member of obj1:", obj1._Base__b)  # Output: 3
print("Accessing private member of obj3:", obj3._Base__b)  # Output: 3

# Printing private member outside
print("Accessing private member of obj4:", obj4._Base__b)  # Output: 3
