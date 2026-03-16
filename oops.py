#oops:
#In python it is a programming style where we use clases and object to organize code
#reusable and user structured
#class=blueprint for creating objects
#object=instance of class
#class:
class student:
    name="john"
    def display (self):
        print(self.name)
#object:
s1=student()
s1.display()
        
        #python automatically passes the object to self
#self:
        #refernce of current object of the class
        #it is used to access variable and methods inside the class
        #s1=object
        #self=refers to s1
#ABSTRACTION:
#hiding internal implementation showing only the essential
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod  # decorator
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("car started")

c = car()   # create object
c.start()   # call method
#payment
#func=pay
#class=credit caard,upi
print("PAYMENT")
from abc import ABC ,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class creditcard(payment):
     def pay(self):
        print("Payment successfull")
class upi(payment):
    def pay(self):
        print("UPI ADDED ")
        
c=creditcard()
c.pay()
u=upi()
u.pay()
#CONSTUCTOR:
#constructor in python is a special method that is automatically called when an object is created from a class
#it is main purpose to initialize (assign values to)the object variables
#__init__()
#syntax
#class classname:
       #def __init__(self,parameters)
       #initialize the code
#eg:
class student:
    def __init__(self):
        print("constuctor is called")
#types of constructor:
        #default=no argument
        #parameterized=with argument
#without constructor:
class student:
    def demo(self,name,age):
        self.name=name
        self.age=age
    

s1=student()
s1.demo("Arun",20)
print(s1.name)
#init:constructor
#INHERITANCE:
 #reuse
#it allows one class to use the properties and method of another class
#parent class---->base class
#child class---->Derived /Subclass
#syntax:
#class parentclass:
   #parent properties
#class childclass(parent class)
class Animal :
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(Self):
        print("Dog is Barking")
d=Dog()
d.eat()
d.bark()
#ACCESS MODIFIERS
#PUBLIC
#PRIVATE=--a=PRIVATE
#PROTECTED-a=25
        
class parent:
    def __init__(self):
        self._age=25
class child(parent):
    def show(self):
        print(self._age)
obj=child()
obj.show()
#can be printed in outside function
print(obj._age)

#single inheritance

class company ():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
class employee(company):
    def show(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        

obj=employee("Abarna",22,40000)
obj.show()

#hierarical inheritance:
print("HIERACHAL INHERITANCE:")
class phone():
    def __init__(self,model,price):
        self.model=model
        self.price=price
    
class cameraphone(phone):
    def show(self):
        print(self.model)
        print(self.price)
    
class smartphone(cameraphone):
    def display(self):
        print(self.model)
        print(self.price)
c=cameraphone("NOKIA",7000)
c.show()
s=smartphone("REALME",22000)
s.display()
#MULTILEVEL INHERITANCE
print("MULTILEVEL")
class vehicle():
    def start(self):
        print("car started")
class car(vehicle):
    def drive(self):
        print("start driving")
class electriccar(car):
    def charge(self):
        print("check charge")
        
        
        
v=vehicle()
v.start()
c=car()
c.drive()
e=electriccar()
e.charge()
#polymorphism:
#eg:addition and concatenation --->same procedure differrent behaviour
#one thing many forms
#same method can perform different action
#runtime=overridding
#compile time=over loading
#method overriding:
#same method name in parent class and child class ,but different behaviour
#eg:
class Animal:
    def sound(self):
        print("Animal makes sound")
class dog(Animal):
    def sound(self):
        print("Dog barks")
obj=dog()
obj.sound()
#class display:
   # def show(self):
       # print("This is parent class")
#class demo(display):
   # def show(self):
       # super.show()
       # print("This is child class")
#obj=demo
#obj.show()
#encapsulation:
       #wrapping data(variable)and methods(functions)together inside a class and restricting direct access to the data--->data hding and protection
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

s = Student("Abarna", 90)
s.display()
#GETTER
#SETTER
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private variable

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        self.__marks = marks


s = Student("Abarna", 85)

print("Marks:", s.get_marks())   # using getter

s.set_marks(95)                  # using setter
print("Updated Marks:", s.set_marks())


class student:
    def __init__(self):
        self.__marks=0
    def set_marks(self,m):
        self.__marks=m
    def get_marks(self):
        return self.__marks
obj=student()
obj.set_marks(90)
print(obj.get_marks())
        

   #INTERVIEW QUESTIONS: 

       #reverse
       #factorial
       #palindrome
       #prime
       #lambda
       #fibonacci
       #abstraction
       #factorial
       #module






































