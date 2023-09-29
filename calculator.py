#NYONGESA METHUSELLA MISIKO
#SCT211-0069/2022
from datetime import date
def add(num1, num2) :
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1,num2):
    return num1/num2
def modulus(num1,num2):
    return num1%num2

print("Select Operation -\n" \
      "1 Add\n" \
      "2 Subtract\n" \
      "3 Multiply\n" \
      "4 Divide\n" \
      "5 Modulus\n")

select = int(input("Select operations form 1, 2, 3, 4, 5 :"))

number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/",
         number_2, "=", divide(number_1, number_2))
elif select == 5:
    print(number_1, "%", number_2, "=", modulus(number_1, number_2))

else:
    print("Invalid input")



# Function to calculate age
def calculate_age(year_of_birth):
    today = date.today()
    birth_date = date(year_of_birth, 1, 1)  
    age = today.year - year_of_birth - ((today.month, today.day) < (1, 1))
    
    # Calculate months and days
    months = today.month - 1 if today.day < birth_date.day else today.month
    days = today.day - birth_date.day if today.day >= birth_date.day else (30 - birth_date.day) + today.day

    return age, months, days

# Get year of birth from the user
year_of_birth = int(input("Enter your year of birth: "))

# Calculate age
age, months, days = calculate_age(year_of_birth)

# Display the results
print(f"Your age is {age} years, {months} months, and {days} days.")

