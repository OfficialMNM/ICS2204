# Function to calculate the total amount per person
def calculate_split_bill(total_bill, tip_percentage, num_people):
    # Calculate the tip amount
    tip_amount = total_bill * (tip_percentage / 100)
    
    # Calculate the total bill including the tip
    total_with_tip = total_bill + tip_amount
    
    # Calculate the amount per person
    amount_per_person = total_with_tip / num_people
    
    return amount_per_person

# Get user input
total_bill = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))

# Validate tip percentage
if tip_percentage not in [10, 12, 15]:
    print("Invalid tip percentage. Please enter 10, 12, or 15.")
else:
    # Calculate the total amount per person
    amount_per_person = calculate_split_bill(total_bill, tip_percentage, num_people)

    # Display the result rounded to two decimal points
    print(f"Each person should pay: ${amount_per_person:.2f}")
