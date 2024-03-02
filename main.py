# import helper
#  import helper as h
# from helper import *
from helper import validate_and_execute
user_input = ""
#while loop
while user_input != "exit":
    #Get user input
    user_input = input("Hey user, enter number of days and conversion unit!\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days":days_and_unit[0],"unit":days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)
