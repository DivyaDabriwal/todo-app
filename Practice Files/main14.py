import json

with open("files/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    correctAnswer = question["correct_answer"]
    if user_choice == correctAnswer:
        print("Right Answer")
    else:
        print('Wrong Answer')
