from datetime import date

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi_rounded}")
print(f"Category: {category}")

# Save to file
today = date.today()
with open("bmi_history.txt", "a") as file:
    file.write(f"{today} | Weight: {weight}kg | Height: {height}m | BMI: {bmi_rounded} | {category}\n")

print("Saved to bmi_history.txt!")