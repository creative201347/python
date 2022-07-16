# 100 Days of Python Learning || Day3

In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

Main Concepts of Object-Oriented Programming (OOPs)

- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance
- Data Abstraction

## Class

A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.

- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

```
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
```

The `__init__` is a special method, known as a Constructor, is used to initialize the class with attributes.

## Object

An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values. Objects are basically an encapsulation of data variables and methods acting on that data into a single entity.

```
emp_1 = Employee('fname', 'lname', 500000)
emp_2 = Employee('fname', 'lname', 600000)
print(emp_1.fullname(), emp_1.pay)
print(emp_2.fullname(), emp_2.pay)
```

## Encapsulation

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).\
It describes the idea of wrapping data and the methods that work on data within one unit.\
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.\
To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.\
`A class is an example of encapsulation as it encapsulates all the data i.e member functions, variables, etc.`

```
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

```

## Inheritance

Inheritance is the capability of one class to derive or inherit the properties from another class.\
The class that derives properties is called the derived class and the class from which the properties are being derived is called the base class.

## Polymorphism

Polymorphism in Python is the ability of an object to take many forms. In simple words, polymorphism allows us to perform the same action in many different ways.

## Data Abstraction

It hides the unnecessary code details from the user. Also, when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.
Data Abstraction in Python can be achieved through creating abstract classes.

## Magic Methods

Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. **These are commonly used for operator overloading**. Few examples for magic methods are: `__init__, __add__, __len__, __repr__` etc.

The` __init__` method for initialization is invoked without any call, when an instance of a class is created, like constructors in certain other programming languages such as C++, Java, C#, PHP etc. These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.

## @classmethod

The `@classmethod` decorator is a built-in function decorator that is an expression that gets evaluated after your function is defined. The result of that evaluation shadows your function definition. A class method receives the class as an implicit first argument, just like an instance method receives the instance

- A class method is a method that is bound to the class and not the object of the class.
- They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
- It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.

## @staticmethod

A `@staticmethod` does not receive an implicit first argument. A static method is also a method that is bound to the class and not the object of the class. This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.

## Class method vs Static Method

- A class method takes cls as the first parameter while a static method needs no specific parameters.
- A class method can access or modify the class state while a static method can’t access or modify it.
- In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
- We use `@classmethod` decorator in python to create a class method and we use `@staticmethod` decorator to create a static method in python.
- We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
- We generally use static methods to create utility functions.
