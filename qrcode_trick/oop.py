# # parnt class
# class Person(object):
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber

#     def display(self):
#         print(self.name)
#         print(self.idnumber)

#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))


# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post

#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)

#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))


# a = Employee("Rahul", 886012, 200000, "Intern")
# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()

# polymerphism


# class Bird:
#     def intro(self):
#         print("There are many types of birds.")

#     def flight(self):
#         print("Most of the birds can fly but some cannot.")


# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")


# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")


# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()

# data encapsulation
# Python program to
# demonstrate private members


# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")

    # print(self.__c)


# Driver code
obj1 = Derived()


# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
