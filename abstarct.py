from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# # s=Animal()
# # s.sound() 
# class Dog(Animal):
#    def sound(Self):
#     print("bow")
# s1=Dog()
# s1.sound()  
# class Parent(ABC):
#     @abstractmethod
#     def greet(self):
#         pass
# class Child1(Parent):
#     def greet(self):
#         print("hi")
# s3= Child1()   
# # # s3.greet()
# class employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
# class wage(employee):
#     def calculate_salary(Self,salary,workingdays):
#         Self.s=salary
#         Self.w=workingdays
#         print(Self.s*Self.w)
# s=wage()
# s.calculate_salary(12000,2)
# class bankaccount(ABC):
#     @abstractmethod
#     def withdraw():
#         pass
# class  bank:
#     def withdraw(self,)           
# try:
#     print("first line")
#     print(10/2)       #here there is a error
#     print("this line")
# except:
#     print("error has in your block")   #that error will handle by except
# # print("hello this sandhya")
# else:
#     print("hii this harish" ) #if there is no error else part will execute
# try:
#     print("first line")
#     print(10/2)       #here there is a error
#     print("this line")
# except:
#     print("error has in your block")   #that error will handle by except
# # print("hello this sandhya")
# else:
#     print("i am learning python")
# finally:
#     print("hii this harish" ) #if error is there it will print if there is no error it will also print it doesn't take care of except(error)
# try:
#     file = open("sales.csv", "r")

# except FileNotFoundError:
#     print("Dataset Not Found")
# # age=int("abc")
# # print(age)   
# try:
#     age=int("abc")
# except ValueError: 
#     print("invalid numeric value")
class Bankaccount(ABC):
    @abstractmethod
    def withdraw(self,available,cash):
        pass  
class banks(Bankaccount):           
    def withdraw(self,available,cash):
       if available>=cash:
        return(cash)     
       else:
        return("insufficient balance")
b=banks()
print(b.withdraw(25000,12000))
print(b.withdraw(26000,28000))
class Student(ABC):
    @abstractmethod
    def grade(self,marks):
        pass
class Section(Student):
    def grade(self,marks):
        if marks>=90:
            return ("your marks is:",marks,"your grade is:A")
        elif marks>=75:
            return("your marks is:",marks,"your grade is:B")
        elif marks>=50:
            return("your marks is:",marks,"your grade is:c")
        else:
            return("your marks is:",marks,"fail")
card=Section()
print(card.grade(60))
print(card.grade(45))                    
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self,length,width,side):
        pass


class Rectangle(Shape):
    def area(self,length,width,side):
        return length * width


class Square(Shape):

    def area(self,length,width,side):
        return side * side


r=Rectangle()
print(r.area(5,4,3))
S=Square()
print(S.area(5,4,3))
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        return "Payment successful through UPI"
class Creditcard(Payment):
    def pay(self):
        return "Payment successful using Credit Card."
class Netbanking(Payment):
    def pay(self):
        return "Payment successful through Net Banking."
u=UPI()
print(u.pay()) 
c=Creditcard()
print(c.pay())
n=Netbanking()
print(n.pay())                      
class Vehicle(ABC):
    @abstractmethod
    def Speed(self):
        pass
class Bike(Vehicle):
    def Speed(self):
        return "Bike speed is 80KM/h"
class Car(Vehicle):
    def Speed(self):
        return "Car speed is 120KM/h"
c=Car()
b=Bike()
print(c.Speed())
print(b.Speed())
class Marks(ABC):
    @abstractmethod
    def  result(self,marks):
        pass
class reportcard(Marks):
    def result(self,marks):
        if marks>=35:
            print("pass")
         
        else:
            print("fail")
c=reportcard()
c.result(55) 
class ElectricityBill(ABC):
    @abstractmethod
    def calculate_bill(self,unit,rateperunit):
        pass
class Bill(ElectricityBill):
    def calculate_bill(self,unit,rateperunit):
        amount=unit*rateperunit
        return("electicitybill",amount)
B=Bill()
print(B.calculate_bill(50,20))      
class Employee(ABC):
    @abstractmethod
    def bonus(self,salary):
        pass
class PlusSalary(Employee):
    def bonus(self,salary):
        if salary>=50000:
            return salary+(salary*20/100)
        else:
            return salary+(salary*10/100) 
p=PlusSalary()
print(p.bonus(60000))                                
print(p.bonus(12000))