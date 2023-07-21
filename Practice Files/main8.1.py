calculate = 0
flip = 0
# formula = calculate/flip*100

with open("Calculator", "w") as file:

    while True:
        user_input = input("Throw the coin and enter head or tail here: ? ")
        match user_input:
            case "head":
                calculate += 1
                flip += 1
            case "tail":
                flip += 1
            case "exit":
                break
        print(f"Heads: {calculate/flip*100}%")
        file.write(f"Heads: {calculate/flip*100}% \n")
