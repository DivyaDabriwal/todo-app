user_prompt = "Please enter the password : "
user_input = input(user_prompt)

user_prompt1 = "Please re-enter the password : "
user_input1 = input(user_prompt1)

while user_input != user_input1:
    user_input1 = input(user_prompt1)
