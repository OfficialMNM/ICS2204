def add(num1, num2) :
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1,num2):
    return num1/num2

print("Select Operation -\n" \
      "1 Add" \
      "2 Subtract" \
      "3 Multiply" \
      "4 Divide\n" )

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == 1:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))

else:
    print("Invalid input")