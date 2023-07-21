def calculate_meters(feet_inches_local):
    product_list = feet_inches_local.split(" ")
    feet = int(product_list[0])
    inches = int(product_list[1])
    calculation = feet * 0.3048 + inches * 0.0254
    return calculation


feet_inches = input("Enter feet and inches : ")
print(f'{calculate_meters(feet_inches)} meters')

