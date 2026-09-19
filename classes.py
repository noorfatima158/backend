# classes
# _init_() method 
class Student:
    def __init__(self, name, age):
        self.name = name       #store info in object (self constructor)
        self.age = age

student1 = Student("Noor", 22)

print(student1.name)
print(student1.age)

#inheritence 

class person:
    def __init__(self , name , age):      #parent class
        self.name = name
        self.age = age 

    def myname(self):                       #function of class 
        print("my name is ", self.name)
    def myage(self):
            print("my age is ", self.age)

a=person("noor ", 22)
a.myname()
a.myage()


#child class 

class student(person):
     pass 
b=student("fizza", 21)       #properties inherited to child class 
b.myname()
b.myage()


#polymorphism

class cat:
     def sound(self):
      print("meow")

class dog:
    def sound(Self):
        print("bark")

cat=cat()
dog=dog()
cat.sound()
dog.sound()


#encapsulation

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show_age(self):
        print(self.__age)


student = Student("Noor", 22)
print(student.name)
print(student.__age)             #error (can't be accessed directly )
student.show_age()