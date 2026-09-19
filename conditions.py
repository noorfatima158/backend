# conditoons 
name = "noor "
age =20
cgpa =3.96
is_student= True

print(name)
print(age)
print(cgpa)
# functions
def display_cgpa():
    print("cgpa" , cgpa)

def display_age():
    print("age", age )

def display_name():
    print("name", name)

display_name()
display_age()
display_cgpa()

# use of conditional statement
if age>10:
    print("eligible")
#if statement


if cgpa>3.8:
    print("pass")
else:
    print("fail")
#if else statement 

if is_student == True:
    if cgpa>3.5:
        print( name , "is eligible for scholarship ")
    else:
        print ( name , "is not eligible ")

# nested if statement 

if cgpa >= 3.9:
    print("excellent")

elif cgpa > 3.8:
    print("good")

elif cgpa > 3.7:
    print("okishhhh")

else:
    print("need improvement")


