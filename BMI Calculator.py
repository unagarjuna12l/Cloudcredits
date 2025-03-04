def calculate_bmi(weight, height, weight_unit="kg", height_unit="m"):
    """Calculates BMI."""
    if weight_unit == "lbs":
        weight = weight * 0.453592
    if height_unit == "ft":
        height = height * 0.3048
    if height <= 0 or weight <= 0:
        return None
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """Interprets BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_user_input():
    """Gets user input with error handling."""
    try:
        weight = float(input("Enter your weight: "))
        weight_unit = input("Enter weight unit (kg or lbs): ").lower()
        if weight_unit not in ("kg", "lbs"):
            print("Invalid weight unit. Please enter 'kg' or 'lbs'.")
            return None

        height = float(input("Enter your height: "))
        height_unit = input("Enter height unit (m or ft): ").lower()
        if height_unit not in ("m", "ft"):
            print("Invalid height unit. Please enter 'm' or 'ft'.")
            return None

        return weight, height, weight_unit, height_unit

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return None

def main():
    while True:
        user_input = get_user_input()

        if user_input:
            weight, height, weight_unit, height_unit = user_input
            bmi = calculate_bmi(weight, height, weight_unit, height_unit)

            if bmi is not None:
                print(f"Your BMI is: {bmi:.2f}")
                interpretation = interpret_bmi(bmi)
                print(f"You are: {interpretation}")
            else:
                print("Invalid height or weight entered.")
        else:
            print("Please try again.")

        another_calculation = input("Do you want to calculate another BMI? (yes/no): ").lower()
        if another_calculation != "yes":
            break #Exit the while loop
        print("") #add a blank line for readability.

if __name__ == "__main__":
    main()
