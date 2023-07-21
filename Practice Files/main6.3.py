filenames = ["one.txt", "two.txt", "three.txt"]

content = "Hello"

for i in filenames:
    file = open(f"files/{i}", "w")
    file.write(content)
    file.close()
    