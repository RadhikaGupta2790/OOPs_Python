class Dog:
    'dog class' #<- comment in class to define class can be writen inside inverted commas
    #class attributes
    species = "Canis familiaris" 
    listzt = ['j','h']
    
    #this is a constructor and a dunder method
    #dunder methood starts and ends with __
    def __init__(self, name, age):
        #instance attributes
        self.name = name
        self.age = age
    
D = Dog('A',22)
print("class without __str__",D)
# class without __str__ <__main__.Dog object at 0x7f262e482d50>
print(D.species,",",D.name,D.listzt)
# Canis familiaris , A ['j', 'h']

class Cat(Dog):
    'cat class'
    animal = "animal"
    def __init__(self, name, age):
        super().__init__(name,age)
        self.listzt.append('gggg')
        self.listzt.remove('j')
        self.mmm = "pet " + Cat.animal 
        
    #this is a dunder method 
    #when defined  instead of object location you get what you have defined here.
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
C = Cat('Bb',22)
print("class with __str__",C)
# class with __str__ Bb is 22 years old
print(C.species,",",C.name,",",C.mmm,",",C.species, C.listzt)
# Canis familiaris , Bb , pet animal , Canis familiaris ['h', 'gggg']
print(type(C))   
# <class '__main__.Cat'>
print(isinstance(D, Cat))
# False
print(isinstance(D, Dog))
# True
