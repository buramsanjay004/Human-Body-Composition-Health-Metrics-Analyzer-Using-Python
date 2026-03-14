weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))
age = int(input("Enter age: "))
waist = float(input("Enter waist circumference (cm): "))
hip = float(input("Enter hip circumference (cm): "))
gender = input("Enter gender (male/female): ").lower()


def bmi(weight, height):
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)


def whr(waist, hip):
    return round(waist / hip, 2)


def wht_ratio(waist, height):
    return round(waist / height, 2)


def body_fat(weight, height, age, gender):
    height_m = height / 100
    bmi_value = weight / (height_m ** 2)

    if gender == "male":
        bf = (1.20 * bmi_value) + (0.23 * age) - 16.2
    else:
        bf = (1.20 * bmi_value) + (0.23 * age) - 5.4

    return round(bf, 2)


def bmr(weight, height, age, gender):
    if gender == "male":
        return round(10 * weight + 6.25 * height - 5 * age + 5, 2)
    else:
        return round(10 * weight + 6.25 * height - 5 * age - 161, 2)


def lean_body_mass(weight, height, age, gender):
    bf = body_fat(weight, height, age, gender)
    return round(weight * (1 - bf / 100), 2)


def bmi_category(bmi_value):
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal Weight"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"


def diet_suggestion(bmi_value):
    if bmi_value < 18.5:
        return "Increase calorie intake and eat protein-rich foods."
    elif bmi_value < 25:
        return "Maintain balanced diet with fruits, vegetables and proteins."
    else:
        return "Reduce sugar and processed foods. Increase exercise."


# Calculations
bmi_value = bmi(weight, height)
body_fat_value = body_fat(weight, height, age, gender)
whr_value = whr(waist, hip)
wht_value = wht_ratio(waist, height)
bmr_value = bmr(weight, height, age, gender)
lbm_value = lean_body_mass(weight, height, age, gender)

# Output
print("\n----- Body Health Report -----")

print("BMI:", bmi_value)
print("BMI Category:", bmi_category(bmi_value))

print("Body Fat %:", body_fat_value)

print("Waist-Hip Ratio:", whr_value)
print("Waist-Height Ratio:", wht_value)

print("BMR (Calories/day):", bmr_value)

print("Lean Body Mass:", lbm_value, "kg")

print("\nDiet Suggestion:")
print(diet_suggestion(bmi_value))


