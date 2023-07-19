try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    calculation = value / total_value * 100

    print(f"That is {calculation}%")

except ValueError:
    exit("You need to enter a number. Run the program again.")
