#Refered from : ChatGpt

class BaseClass:
    def __init__(self):
        self._protected_variable = 42  # Protected variable
        self.__private_variable = 100  # Private variable

    def _protected_method(self):
        print("This is a protected method in BaseClass")

    def __private_method(self):
        print("This is a private method in BaseClass")

    def public_method(self):
        print("This is a public method in BaseClass")
        self._protected_method()
        self.__private_method()


class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()

    def _protected_method(self):
        # Overriding the protected method from the base class
        print("This is an overridden protected method in DerivedClass")

    def public_method(self):
        print("This is a public method in DerivedClass")
        # Accessing the protected variable from the base class
        print("Protected variable from base class:", self._protected_variable)
        # Calling the protected method from the base class
        self._protected_method()
        # Accessing the private variable from the base class
        # Note: This will raise an AttributeError because private variables are not directly accessible in subclasses
        # print("Private variable from base class:", self.__private_variable)
        # Calling the private method from the base class
        # Note: This will raise an AttributeError for the same reason
        # self.__private_method()


# Creating instances
base_instance = BaseClass()
derived_instance = DerivedClass()

# Accessing protected variables and methods
print("Protected variable from base instance:", base_instance._protected_variable)
base_instance._protected_method()

# Accessing public variables and methods
print("\nPublic method from base instance:")
base_instance.public_method()

# Accessing protected variables and methods in the derived class
print("\nProtected variable from derived instance:", derived_instance._protected_variable)
derived_instance._protected_method()

# Accessing public variables and methods in the derived class
print("\nPublic method from derived instance:")
derived_instance.public_method()



'''
O/P
Protected variable from base instance: 42
This is a protected method in BaseClass

Public method from base instance:
This is a public method in BaseClass
This is a protected method in BaseClass
This is a private method in BaseClass

Protected variable from derived instance: 42
This is an overridden protected method in DerivedClass

Public method from derived instance:
This is a public method in DerivedClass
Protected variable from base class: 42
This is an overridden protected method in DerivedClass
'''
