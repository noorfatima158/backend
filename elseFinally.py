try:
    number = int(input("Enter a number: "))
    print("You entered", number)

except:
    print("Invalid input")

else:
    print("Everything worked successfully")

#checking for error example

try:
    number = 10 / 2
    print(number)

except:
    print("Something went wrong")

finally:
    print("This always runs")