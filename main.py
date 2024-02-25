# Declaring variables globally
calculation_to_units = 24
name_of_units = "hours"

# Define a function
def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}"


# Call the function
# days_to_units(100)
    
# Validate user input with conditional statement and comparison operator
def validate_and_execute():
    # if user_input.isdigit():
    try:
        #Cast the string input into number
        user_input_to_number = int(user_input)
        if user_input_to_number > 0:
            calculated_value = days_to_units(user_input_to_number) 
            print(calculated_value)
        elif user_input_to_number == 0:
             print("You entered 0, please enter a valid positive number")
        else:
            print("You entered a negative value, no conversion for you")
    except ValueError:
        print("Your input is not a valid number, Dont ruin my program!")

user_input = ""
#while loop
while user_input != "exit":
    #Get user input
    user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
    # function call
    validate_and_execute()

