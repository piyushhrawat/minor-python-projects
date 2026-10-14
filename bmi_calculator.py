import numpy as np

class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

# Calculate BMI using the formula: BMI = weight (kg) / (height (m))^2
    def calculate_bmi(self):
        if self.height <= 0:
            return "Error! Height must be greater than zero."
        
        elif self.weight <= 0:
            return "Error! Weight must be greater than zero."
        
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

# Check if the BMI falls into a specific category
    def bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"


# Take input from user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Create an instance of BMICalculator and calculate BMI
bmi_calculator = BMICalculator(weight, height)
bmi_result = bmi_calculator.calculate_bmi()

# Check category only if BMI is valid (not an error string)
if isinstance(bmi_result, float):
    category = bmi_calculator.bmi_category(bmi_result)
    print(f"Your BMI is: {bmi_result} ({category})")
else:
    print(bmi_result)
