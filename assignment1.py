#question no 1
age =int(input("enter the age="))

if age<18:
    print("you are minor ")
elif 18<=age<=65:
    print("you are adult")
else:
    print("you are senior citizen")

#question no 2
n1=float(input("enter the first number "))
n2=float(input("enter the second number"))
opr=input("enter the operator").strip()

match opr:
    case'+':
        result=n1+n2
    case'-':
        result=n1-n2
    case'*':
        result=n1*n2
    case'/':
        if n2==0:
            print("math error")
        else:
            result=n1/n2
    case _:
        print("invalid operator ")


#question no 3
a=int(input("enterbthe term(n):"))
if a<=0:
    print("invalid input . enter valid positive integer")
elif a==1 :
    print("fibonacci sequence:0")
else:
    fib_sequence=[]
    a,b=0,1
    for _ in range(n):
     fib_sequence.append(a)
     a,b=b,a+b
print("fibonancci sequence:",",".join(map(str,fib_sequence)))