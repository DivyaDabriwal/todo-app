# Condition:
# 1. At least 8 characters long
# 2. At least 1 uppercase letter
# 3. At least 1 digit


user_input = input("Enter new password: ")

condition_1 = len(user_input) > 8
condition_2 = False
condition_3 = False

for i in user_input:
    if i.isupper():
        condition_2 = True

for i in user_input:
    if i.isdigit():
        condition_3 = True

if condition_1 and condition_2 and condition_3 is True:
    print("Strong Password")
else:
    print("Weak Password")
