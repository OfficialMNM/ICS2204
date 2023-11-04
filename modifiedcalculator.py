name = input("Enter your name:")

greeting = "Hello, " + name
print(greeting)
class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "MATH ERROR"
        return num1 / num2

    def modulus(self, num1, num2):
        return num1 % num2

def main():
    calculator = Calculator()

    print("Enter Options between 1 and 5:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for modulus")

    user_data = input(":")
    
    if user_data in ["1", "2", "3", "4", "5"]:
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))

        if user_data == "1":
            result = calculator.add(num1, num2)
        elif user_data == "2":
            result = calculator.subtract(num1, num2)
        elif user_data == "3":
            result = calculator.multiply(num1, num2)
        elif user_data == "4":
            result = calculator.divide(num1, num2)
        elif user_data == "5":
            result = calculator.modulus(num1, num2)

        print("Result: " + str(result))
    else:
        print("Syntax Error")

if __name__ == "__main__":
    main()
