from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon ex:Learn React:06.03.2024\n")
input_list  = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline,"%d.%m.%Y")
today_date = datetime.today()

#Calculate how many days from now till deadline
time_till_deadline = deadline_date - today_date

hours_till_deadline = int(time_till_deadline.total_seconds() / 60 /60)
print(f"Dear user, time remaining for your goal: {goal} is {hours_till_deadline} hours")