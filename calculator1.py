def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

name = input("Enter your name:")

greeting = "Hello, " + name
print(greeting)


print("Select Operation -\n" \
      "1. Add\n" \
      "2. Subtract\n"
      )

Choice = int(input("Select operation from 1, 2:"))

number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))

if Choice == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif Choice == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

else:
    print("Invalid input")
