#define a class
class User:
    def __init__(self,name,email,password,current_job_title):
        self.name = name,
        self.email = email,
        self.password = password,
        self.current_job_title = current_job_title,
    
    def change_password(self,new_password):
        self.password = new_password

    def change_job_title(self,new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"I'm {self.name}, I currently work as a {self.current_job_title}. YOu can contact me at {self.email}")

#Class instantiation should be done in a separate file
#Create an instance of the user class
app_user_one = User("Kay","kay@kay.com","password","Software Developer")
app_user_one.get_user_info()

#Change the job title
app_user_one.change_job_title("Software Engineer")
app_user_one.get_user_info()