def days_to_units(number_of_days,conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} {conversion_unit}"
    elif conversion_unit== "minutes":
        return f"{number_of_days} days are {number_of_days * 24*60} {conversion_unit}"
    else:
        return

# Call the function
# days_to_units(100)
    
# Validate user input with conditional statement and comparison operator
def validate_and_execute(days_and_unit_dictionary):
    # if user_input.isdigit():
    try:
        #Cast the string input into number for positive integers
        user_input_to_number = int(days_and_unit_dictionary["days"])
        if user_input_to_number > 0:
            calculated_value = days_to_units(user_input_to_number,days_and_unit_dictionary["unit"]) 
            print(calculated_value)
        elif user_input_to_number == 0:
             print("You entered 0, please enter a valid positive number")
        else:
            print("You entered a negative value, no conversion for you")
    except ValueError:
        print("Your input is not a valid number, Dont ruin my program!")
