def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


while True:
    print("\n========== BMI CALCULATOR ==========")

    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            continue

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    choice = input("\nDo you want to calculate again? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for using the BMI Calculator!")
        break

















