# Declaring variables globally
calculation_to_units = 24
name_of_units = "hours"

# Define a function
def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_units}"

# Call the function
# days_to_units(100)

#Get user input
user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
calculated_value = days_to_units(int(user_input)) #Cast the string input into number
print(calculated_value)