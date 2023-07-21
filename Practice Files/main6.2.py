user_input = input("Add a new member: ")

file = open("files/members.txt", "r")
content = file.readlines()
file.close()

content.append(f"\n{user_input}")

file = open("files/members.txt", "w")
file.writelines(content)
file.close()
