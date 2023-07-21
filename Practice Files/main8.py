# Enter today's date: 2022-10-20
# How do you rate your mood today from 1 to 10? 8
# Let your thoughts flow:
# It was a good day in general. No big events happened.

input_date = input("Enter today's date: ")
input_mood = input("How do you rate your mood today from 1 to 10? ")
input_thoughts = input("Let your thoughts flow: \n")

with open(input_date, 'w') as file:
    file.writelines(input_mood + 2 * "\n")
    file.writelines(input_thoughts)
