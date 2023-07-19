open_filenames = ["a.txt", "b.txt", "c.txt"]
content = []

for txtFile in open_filenames:
    file = open(f"files/{txtFile}", "r")
    context = file.read()
    content.append(context)
    file.close()

for i in content:
    print(i)

for filename in open_filenames:
    file = open(f"files/{filename}", "r")
    print(file.read())
    file.close()
