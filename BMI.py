# Function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Function to determine BMI category
def determine_bmi_category(bmi):
    if bmi < 18:
        return "Underweight"
    elif 18 <= bmi < 24:
        return "Normal Weight"
    else:
        return "Overweight"

# Get user input
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight_kg, height_m)

# Determine BMI category
bmi_category = determine_bmi_category(bmi)

# Display the result
print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the {bmi_category} category.")
