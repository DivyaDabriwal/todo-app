def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius_d = get_maximum()
fahrenheit = celsius_d * 1.8 + 32

print(fahrenheit)
